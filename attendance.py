import itertools


class GraduationAttendanceProbability:

    def __init__(self, total_days, absence_allowed):
        self.total_days = total_days
        self.absence_allowed = absence_allowed

    def __get_total_attendance_combinations(self):
        """
        this functions ia to get list of all the possible combination of attendance for n days
        """

        absent, present = 0, 1
        options = [absent, present]
        return [
            combination
            for combination in itertools.product(options, repeat=self.total_days)
        ]

    def __check_valid_attendance_series(self, attendance_series):
        """
        This function is to check if the attendance series is valid. i.e.,
        if the attendance series allows the student to attend graduation or not.

        inp: accepts individual attendance series
        ex: if n =5, attendance_series = (0,0,0,0,0)

        op: Boolean
        """

        consecutive_absent = 0
        prev = attendance_series[0]
        if prev == 0:
            consecutive_absent += 1
        for i in range(1, len(attendance_series)):
            if attendance_series[i] == 1:
                prev = attendance_series[i]
                consecutive_absent = 0
                continue
            else:
                consecutive_absent += 1
                if consecutive_absent >= 4:
                    return False
        return True

    def __get_total_valid_combinations(self):
        """
        This function is to filter out only valid attendance combinations that
        allows the student to be eligible to attend graduation.

        op: List of valid combinations
        """

        total_possible_attendance_combinations = (
            self.__get_total_attendance_combinations()
        )
        return [
            attendance_combination
            for attendance_combination in total_possible_attendance_combinations
            if self.__check_valid_attendance_series(attendance_combination)
        ]

    def __get_total_graduation_miss_possibility(self):
        """
        This function is to filter out the combinations that might cause the students
        to miss graduation day, assuming that the last day is the graduation day.
        """

        valid_attendance_combinations = self.__get_total_valid_combinations()
        count = 0
        for i in valid_attendance_combinations:
            if i[-1] == 0:
                count += 1
        return count

    def prob_miss_graduation(self):
        """
        This function returns the probability of attendance series that might cause the
        students to miss graduation and total valid attendance combination that keeps
        the students eligible to attend graduation.
        """

        valid_attendance_combinations = self.__get_total_valid_combinations()
        possible_graduation_miss = self.__get_total_graduation_miss_possibility()
        return "{}/{}".format(
            possible_graduation_miss, len(valid_attendance_combinations)
        )


if __name__ == "__main__":
    days = 10
    abs_limit = 4
    obj = GraduationAttendanceProbability(days, abs_limit)
    print(obj.prob_miss_graduation())
