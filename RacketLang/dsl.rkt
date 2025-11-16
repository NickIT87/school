#lang racket

;; Определяем макрос todo
(define-syntax-rule (todo title tasks ...)
  (begin
    (displayln (string-append "TODO: " title))
    ;; правильно распаковываем tasks с "..."
    (for-each (lambda (task) (displayln (string-append "  - " task)))
              (list tasks ...))))


;; Используем DSL
(todo "Сделать домашку"
      "Написать отчет"
      "Сделать упражнения"
      "Проверить почту")

(todo "сходить в магазин")
