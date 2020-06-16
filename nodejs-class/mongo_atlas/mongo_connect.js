const MongoClient = require('mongodb').MongoClient;

// replace the uri string with your connection string.
const uri = "mongodb+srv://kevin87011111:example@cluster0-b9pzv.gcp.mongodb.net/test"
MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true },function(err, client) {
   if(err) {
        console.log('Error occurred while connecting to MongoDB Atlas...\n',err);
   }
   console.log('Connected...');

  //  var stream_A_status = "safe";
  //  var stream_A_status = "warning";

   var dbo = client.db("stream_IoT");

   var myquery = { stream_name: "A" };

   var newvalues = { $set: {stream_name: "A", stream_A_status: stream_A_status } };


//    dbo.collection("object_status").insertOne(myquery, function(err, res) {
//     if (err) throw err;
//     console.log("1 document inserted");
//     client.close();
//   });

   dbo.collection("object_status").find(myquery).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    client.close();
  });

  //  dbo.collection("object_status").updateOne(myquery, newvalues, function(err, res) {
  //   if (err) throw err;
  //   console.log("1 document updated");
  // });
  //  client.close();
});