mkdir input
mkdir output
mkdir detailed
mkdir show-random

curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/random-numbers" > random-numbers.txt

cd input
for i in {1..7}
  do
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/input-$i" > input-$i.txt
  done
cd ..

cd output
for i in {1..7}
  do
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/fcfs-output-$i" > fcfs-output-$i.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/rr-output-$i" > rr-output-$i.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/sjf-output-$i" > sjf-output-$i.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/hprn-output-$i" > hprn-output-$i.txt
  done
cd ..


cd detailed
for i in {1..7}
  do
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/fcfs-output-$i-detailed" > fcfs-output-$i-detailed.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/rr-output-$i-detailed" > rr-output-$i-detailed.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/sjf-output-$i-detailed" > sjf-output-$i-detailed.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/hprn-output-$i-detailed" > hprn-output-$i-detailed.txt
  done
cd ..


cd show-random
for i in {1..7}
  do
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/fcfs-output-$i-show-random" > fcfs-output-$i-show-random.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/rr-output-$i-show-random" > rr-output-$i-show-random.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/sjf-output-$i-show-random" > sjf-output-$i-show-random.txt
    curl "http://cs.nyu.edu/~gottlieb/courses/os202/labs/lab2/hprn-output-$i-show-random" > hprn-output-$i-show-random.txt
  done
cd ..
