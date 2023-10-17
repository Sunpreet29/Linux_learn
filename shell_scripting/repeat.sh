#!bin/bash

function return_function() {
	z=$?
	return $z
}

count=0
while true;
do
	./random.sh
	return_function
	if [[ $z -eq 1 ]]; then
		echo "It took $count times to quit."
		break
	fi
	((count++))
done
echo "The program has been executed $count times."
