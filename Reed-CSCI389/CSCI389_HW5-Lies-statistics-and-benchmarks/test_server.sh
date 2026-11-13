  
echo Testing HEAD: 'curl --head "http://localhost:19134"'
curl --head "http://localhost:19134"
echo

echo Testing PUT/k/v: 'curl -X PUT "http://localhost:19134/a/airplane"'
curl -X PUT "http://localhost:19134/a/airplane"
echo

echo Testing GET/k: 'curl -X GET "http://localhost:19134/a"'
curl -X GET "http://localhost:19134/a"
echo

echo Testing DELETE/k: 'curl -X DELETE "http://localhost:19134/a"'
curl -X DELETE "http://localhost:19134/a"
echo

echo Testing POST/reset: 'curl -X POST "http://localhost:19134/reset"'
curl -X POST "http://localhost:19134/reset"
echo

echo

echo Add three elements to cache, PUT.
curl -X PUT "http://localhost:19134/abc/alpha1"
curl -X PUT "http://localhost:19134/def/alpha2"
curl -X PUT "http://localhost:19134/ghi/alpha3"
echo

echo Confirm space-used is 21, HEAD.
curl --head "http://localhost:19134"
echo

echo Get each of the elements in turn, GET.
curl "http://localhost:19134/abc"
curl "http://localhost:19134/ghi"
curl "http://localhost:19134/def"
echo

echo Delete only one of the elements, DELETE.
curl -X DELETE "http://localhost:19134/def"
echo

echo Attempt to delete an element that does not exist, DELETE.
curl -X DELETE "http://localhost:19134/jkl"
echo

echo Confirm that space-used is now 14, HEAD.
curl --head "http://localhost:19134"
echo

echo Reset the whole cache, POST/reset.
curl -X POST "http://localhost:19134/reset"
echo

echo Confirm that space-used is not 0, HEAD.
curl --head "http://localhost:19134/reset"
echo

echo Confirm that trying to GET a not-present key returns an error.
curl -X GET "http://localhost:19134/jkl"
echo

echo Confirm that trying to POST anything but /reset returns NOT FOUND.
curl -X POST "http://localhost:19134/elsewise"
<<<<<<< HEAD
echo
=======
echo
>>>>>>> 8f1c3d1b175816f94500cf2dbe01c4b3ece77039
