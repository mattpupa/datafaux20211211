
/*
// https://firebase.google.com/docs/hosting/functions#set-up-functions
// https://firebase.google.com/docs/functions/http-events

const functions = require('firebase-functions');

// Imports the Google Cloud client library
const PubSub = require('@google-cloud/pubsub');

// Instantiates a client
const pubsubclient = new PubSub({
  projectId: 'datafaux-307421',
  keyFilename: '/Users/Matt/Desktop/Programming/Jekyll/Datafaux/functions/firestoretopubsubkey.json'
});

const topicDR = pubsubclient.topic('projects/datafaux-307421/topics/datasetRequestTopic');
const dataDR = JSON.stringify({foo: 'bar'});
const dataBuffer = Buffer.from(dataDR);
//const dataBuffer = Buffer.from('Hello, world!'); <-- String
const publisher = topicDR.publisher();

// https://googleapis.dev/nodejs/pubsub/latest/Topic.html#publishMessage
// https://googleapis.dev/nodejs/pubsub/latest/google.pubsub.v1.PubsubMessage.html
// https://cloud.google.com/pubsub/docs/publisher
// https://stackoverflow.com/questions/47968777/google-cloud-pubsubtypeerror-state-topic-publish-is-not-a-function


exports.publishPubSubMessage = functions.https.onRequest(async (request, response) => {
  //res.send("Hello, this is a test...Be bop be boop!")

  try {
    const messageId = await publisher.publish(dataBuffer);
    console.log(`Message ${messageId} published.`);

    // https://cloud.google.com/pubsub/docs/subscriber
    // Need to acknowledge message!
    // Need to worry about indempotence using cloud data flow?!?!?!
    response.status(204).send("message published!")

  } catch (error) {
    console.error(`Received error while publishing: ${error.message}`);
    response.status(500).send(error)
    //process.exitCode = 1;
  }
});


/*

exports.makeUppercase = functions.firestore.document('/datasetRequests/{documentId}')
    .onCreate((snap, context) => {
      // Grab the current value of what was written to Firestore.
      const original = snap.data().original;

      // Access the parameter `{documentId}` with `context.params`
      functions.logger.log('Uppercasing', context.params.documentId, original);

      const uppercase = original.toUpperCase();

      // You must return a Promise when performing asynchronous tasks inside a Functions such as
      // writing to Firestore.
      // Setting an 'uppercase' field in Firestore document returns a Promise.
      return snap.ref.set({uppercase}, {merge: true});
    });


exports.getPubSubTopics = functions.https.onRequest(async (request, response) => {
  //res.send("Hello, this is a test...Be bop be boop!")
  pubsubclient.getTopics()
  .then(function(data) {
    const topics = data[0];
    response.status(500).send(topics)
  })
  .catch(function (error) {
    console.log(error)
    response.status(500).send(error)
  })
});

exports.createPubSubTopic = functions.https.onRequest(async (request, response) => {
  //res.send("Hello, this is a test...Be bop be boop!")
  pubsubclient.createTopic('my-third-topic')
  .then(function(data) {
    const mynewtopic = data[0];
    const apiResponse = data[1];
    response.status(500).send("topic created")
  })
  .catch(function (error) {
    console.log(error)
    response.status(500).send(error)
  })
});

exports.createPubSubSubscription = functions.https.onRequest(async (request, response) => {
  //res.send("Hello, this is a test...Be bop be boop!")
  pubsubclient.createSubscription(topicDR, "my-new-subscription")
  .then(function(data) {
    const mynewSubscription = data[0];
    const apiResponse = data[1];
    response.status(500).send("subscription created!")
  })
  .catch(function (error) {
    console.log(error)
    response.status(500).send(error)
  })
});

// https://www.youtube.com/watch?v=DYfP-UIKxH0&list=PLl-K7zZEsYLkPZHe41m4jfAxUi0JjLgSM
exports.sendData = functions.firestore.document('/datasetRequests/{documentId}')
  // snap and context are specific to .onCreate()
  .onCreate(async function (snap, context) {
      // Check console log in firebase console functions page to test function
      console.log(snap.data()); // Should this be inside function or outside?
      // Access the parameter `{documentId}` with `context.params`
      const docId = context.params.documentId; // Do I need this?!?!
      const response = await request({
        uri: WEBHOOK_URL,
        method: 'POST',
        json: true,
        body: snap.data(), // The current value of what was written to Firestore
        resolveWithFullResponse: true,
      });
      // Publishes a message
      try {
        await topic.publish(originalJsoned); //response.data ???
        response.status(200).send('Message sent.');
      } catch (err) {
        console.error(err);
        response.status(500).send(err);
        return Promise.reject(err);
      };
      //// take out section!
      try {
      const messageId = await pubSubClient.topic(topicName).publish(dataBuffer);
      console.log(`Message ${messageId} published.`);
    } catch (error) {
      console.error(`Received error while publishing: ${error.message}`);
      process.exitCode = 1;
    }
});

*/
