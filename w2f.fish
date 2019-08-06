function w2f
	for i in **.wav
		ffmpeg -i (realpath $i) (string replace '.wav' '' (realpath $i)).flac
		rm -f $i
	end
end