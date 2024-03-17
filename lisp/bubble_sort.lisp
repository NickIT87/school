(defun bubble-sort (lst)
  (loop for swapped = t then nil
        do (loop for i below (1- (length lst))
                 when (> (nth i lst) (nth (1+ i) lst))
                 do (rotatef (nth i lst) (nth (1+ i) lst))
                    (setf swapped t))
        until (not swapped))
  lst)

;; Example usage:
(let ((lst '(5 3 8 2 1)))
  (format t "Before sorting: ~a~%" lst)
  (format t "After sorting: ~a~%" (bubble-sort lst)))
