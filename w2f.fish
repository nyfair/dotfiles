function w2f
	for i in **.wav
		ffmpeg -i (realpath $i) -compression_level 8 (string replace '.wav' '.flac' (realpath $i))
		rm -f $i
	end
end
