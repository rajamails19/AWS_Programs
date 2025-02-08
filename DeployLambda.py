const AWS = require('aws-sdk');
const lambda = new AWS.Lambda();

const params = {
  FunctionName: "MyLambdaFunction",
  Runtime: "nodejs18.x",
  Role: "arn:aws:iam::your-account-id:role/execution-role",
  Handler: "index.handler",
  Code: {
    ZipFile: Buffer.from('exports.handler = async (event) => { return "Hello from Lambda!"; };')
  }
};

lambda.createFunction(params, function(err, data) {
  if (err) console.log("Error", err);
  else console.log("Lambda Function Created:", data);
});
