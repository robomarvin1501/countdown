
build:
	g++ -fPIC -shared -O3 rpn_evaluator.cpp -o rpn_evaluator.so

clean:
	rm rpn_evaluator.so

