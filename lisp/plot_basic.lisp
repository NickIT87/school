(load "~/quicklisp/setup.lisp")

(ql:quickload :cl-dot)

(defun create-dot-file (graph)
  (with-open-file (dot-file "graph.dot" :direction :output
                                         :if-exists :supersede
                                         :if-does-not-exist :create)
    (format dot-file "graph MyGraph {
      // Add graph attributes here (optional)

      // Add nodes
      A
      B
      C

      // Add edges
      A -- B
      B -- C
      C -- A
    }")))

(defun visualize-graph ()
  (create-dot-file "MyGraph")
  (uiop:launch-program '("dot" "-Tpng" "-o" "graph.png" "graph.dot")))

(visualize-graph)
