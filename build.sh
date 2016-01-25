# At ~/ (w.r.t fk-fdp-ml)
cd CAFFE # At ~/CAFFE
cd caffe # At ~/CAFFE/caffe
mkdir build 
cd build # At ~/CAFFE/caffe/build
rm -rf *
cmake ..
make
make pycaffe
