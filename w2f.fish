function w2f
	for i in **.wav **.WAV
		ffmpeg -i $i -compression_level 8 (string replace -r -i 'wav$' 'flac' $i)
		rm -f $i
	end
end