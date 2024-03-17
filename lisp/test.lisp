; hello world program using the CLISP language
; sbcl --script test.lisp

(defun factorial (n)
  "Calculate the factorial of a non-negative integer."
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(defun main ()
  "Main function to calculate and print factorial."
  (let ((number 5)) ; Change this to the desired number
    (format t "Calculating factorial of ~A~%" number)
    (let ((result (factorial number)))
      (format t "Factorial of ~A is: ~A~%" number result))))

(main)