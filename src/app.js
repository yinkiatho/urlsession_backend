const express = require('express');
const app = express();
const upload = require('./helpers/multer_config').upload;
const { spawn } = require('child_process');
const bodyParser = require('body-parser');

//run python script
const { PythonShell } = require('python-shell');


app.use(express.json());

app.get('/', (req, res, next) => {
    res.status(200).json({ success: 'Hello Server' });
});

app.post("/lazy-developer", (req, res) => {
    //run lazy-developer.py with json input from req.body
    //res.status(200).json({ success: 'Hello Server' });
    requestData = req.body
    //console.log(requestData)
    const pythonProcess = spawn('python', ['src/lazy_dev.py', JSON.stringify(requestData)]);

    // Handle data from the Python script
    pythonProcess.stdout.on('data', (data) => {
        const jsonString = data.toString().replace(/'/g, '"');
        //console.log(`Python Output: ${data}`);
        //console.log(`Python Output: ${data.toString()}`);
        output = JSON.parse(jsonString)
        res.json(output);
    });

  // Handle errors (if any)
    pythonProcess.stderr.on('data', (data) => {
    console.error(`Error: ${data}`);
    res.status(500).json({ error: 'An error occurred' });
  });
});


app.post("/greedymonkey", (req, res) => {

    let requestData = "";

    req.setEncoding("utf8"); // Set the encoding to UTF-8 for text data

    req.on("data", (chunk) => {
      requestData += chunk; // Collect the chunks of data
    });

    console.log(requestData)

    //console.log(requestData)
    const pythonProcess = spawn('python', ['src/greedy_monkey.py', JSON.stringify(requestData)]);

    // Handle data from the Python script
    pythonProcess.stdout.on('data', (data) => {
        res.type('text/plain').send(data.toString());
    });

  // Handle errors (if any)
    pythonProcess.stderr.on('data', (data) => {
    console.error(`Error: ${data}`);
    res.status(500).json({ error: 'An error occurred' });
  });
    
});


app.post("/digital-colony", (req, res) => {
  requestData = req.body;
  
  //console.log(requestData)
  const pythonProcess = spawn("python", [
    "src/digital_colony.py",
    JSON.stringify(requestData),
  ]);

  // Handle data from the Python script
  pythonProcess.stdout.on("data", (data) => {
    //console.log(data.toString());
    const jsonString = data.toString().replace(/'/g, '"');
    //console.log(`Python Output: ${data}`);
    //console.log(`Python Output: ${data.toString()}`);
    output = JSON.parse(jsonString);
    res.json(output);
  });

  // Handle errors (if any)
  pythonProcess.stderr.on("data", (data) => {
    console.error(`Error: ${data}`);
    res.status(500).json({ error: "An error occurred" });
  });
});


app.post("/airport", (req, res) => {
  requestData = req.body;

  //console.log(requestData);
  const pythonProcess = spawn("python", [
    "src/airport.py",
    JSON.stringify(requestData),
  ]);

  // Handle data from the Python script
  pythonProcess.stdout.on("data", (data) => {
   //console.log("here" + data.toString());
   const jsonString = data.toString().replace(/'/g, '"');
   //console.log(`Python Output: ${data}`);
   //console.log(`Python Output: ${data.toString()}`);
   output = JSON.parse(jsonString);
   res.json(output);
  });

  // Handle errors (if any)
  pythonProcess.stderr.on("data", (data) => {
    console.error(`Error: ${data}`);
    res.status(500).json({ error: "An error occurred" });
  });
});


app.post("/evaluate", (req, res) => {
  //run lazy-developer.py with json input from req.body
  //res.status(200).json({ success: 'Hello Server' });
  requestData = req.body;
  //console.log(requestData)
  const pythonProcess = spawn("python", [
    "src/railway.py",
    JSON.stringify(requestData),
  ]);

  // Handle data from the Python script
  pythonProcess.stdout.on("data", (data) => {
    const jsonString = data.toString().replace(/'/g, '"');
    //console.log(`Python Output: ${data}`);
    //console.log(`Python Output: ${data.toString()}`);
    output = JSON.parse(jsonString);
    res.json(output);
  });

  // Handle errors (if any)
  pythonProcess.stderr.on("data", (data) => {
    console.error(`Error: ${data}`);
    res.status(500).json({ error: "An error occurred" });
  });
});
module.exports = app;
