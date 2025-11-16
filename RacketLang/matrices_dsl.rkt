#lang racket

;; ----------------------------
;; Вспомогательные функции
;; ----------------------------
(define (matrix-add A B)
  (map (lambda (rowA rowB)
         (map + rowA rowB))
       A B))

(define (matrix-mul A B)
  (let ((colsB (apply map list B))) ; транспонируем B для удобства
    (map (lambda (rowA)
           (map (lambda (colB)
                  (apply + (map * rowA colB)))
                colsB))
         A)))

;; ----------------------------
;; DSL макрос
;; ----------------------------
(define-syntax mat-op
  (syntax-rules (+ *)
    [(mat-op + A B) (matrix-add A B)]
    [(mat-op * A B) (matrix-mul A B)]))

;; ----------------------------
;; Пример использования DSL
;; ----------------------------
(define A '((1 2) (3 4)))
(define B '((5 6) (7 8)))

;; Сложение матриц
(define C (mat-op + A B))
;; Умножение матриц
(define D (mat-op * A B))

(displayln "A + B =")
(displayln C) ; => '((6 8) (10 12))

(displayln "A * B =")
(displayln D) ; => '((19 22) (43 50))
