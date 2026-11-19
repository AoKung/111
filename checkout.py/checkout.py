def apply_student_discount(total, is_student):
	#10% student discount
    if is_student:
        return total * 0.90
    return total

if __name__ == "__main__":
    print(apply_student_discount(100, True))
    print(apply_student_discount(100, False))