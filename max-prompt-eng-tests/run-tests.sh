OUTPUT=data3
rm -fr $OUTPUT
mkdir $OUTPUT

# Run the three basic prompt techniques

python intel-zero.py >  $OUTPUT/intel-zero.out
python intel-knowledge-prompting.py > $OUTPUT/intel-knowledge-prompting.out
python intel-prompt-for-prompt.py > $OUTPUT/intel-prompt-for-prompt.out

# Test using Gen AI as a grader of prompt results 
python intel-test-grading.py > $OUTPUT/intel-test-grading1.out
python intel-test-grading.py > $OUTPUT/intel-test-grading2.out
python intel-test-grading.py > $OUTPUT/intel-test-grading3.out

# Apply Gen AI as a grader of the three different prompt techniques
python intel-test-prompts.py > $OUTPUT/intel-test-prompts1.out
python intel-test-prompts.py > $OUTPUT/intel-test-prompts2.out
python intel-test-prompts.py > $OUTPUT/intel-test-prompts3.out

# Apply the grader to provide feedback and improve the result
python intel-pforp-improve.py > $OUTPUT/intel-pforp-improve1.out
python intel-pforp-improve.py > $OUTPUT/intel-pforp-improve2.out
python intel-pforp-improve.py > $OUTPUT/intel-pforp-improve3.out
