(print "Hello from Hy!")

;; (defn factorial [n]
;;   (if (<= n 1)
;;     1
;;     (* n (factorial (- n 1)))))

;; (print (factorial 10000))

;; (defn factorial [n]
;;   (setv result 1)
;;   (for [i (range 1 (+ n 1))]
;;     (setv result (* result i)))
;;   result)

;; (print (factorial 120))  ; => 120

;; (import functools)
;; (import operator)

;; (defn factorial [n]
;;   (functools.reduce operator.mul (range 1 (+ n 1))))

;; (print (factorial 5))  ; => 120

;; (import sys math)

;; ;; Увеличиваем лимит до 100_000 цифр
;; (.set_int_max_str_digits sys 100000)

;; (setv result (.factorial math 10000))
;; (print result)