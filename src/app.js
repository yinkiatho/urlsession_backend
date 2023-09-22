const express = require('express');
const app = express();
const upload = require('./helpers/multer_config').upload;
const { spawn } = require('child_process');

//run python script
const {PythonShell} = require('python-shell');


app.use(express.json());

app.get('/', (req, res, next) => {
    res.status(200).json({ success: 'Hello Server' });
});

app.post("/lazy-developer", (req, res) => {
    //run lazy-developer.py with json input from req.body
    //res.status(200).json({ success: 'Hello Server' });
    requestData = req.body
    const pythonProcess = spawn('python', ['lazy_dev.py', JSON.stringify(requestData)]);

    // Handle data from the Python script
    pythonProcess.stdout.on('data', (data) => {
    console.log(`Python Output: ${data}`);
    res.json({ message: data.toString() });
    });

  // Handle errors (if any)
    pythonProcess.stderr.on('data', (data) => {
    console.error(`Error: ${data}`);
    res.status(500).json({ error: 'An error occurred' });
  });
    
});

app.post('/upload', upload.array('imageUploads', 10), (req, res) => {
    const senderName = req.body.fromName;


    if (senderName == null || senderName == undefined) {
        res.status(500).json({ error: `No senderName sent.` });
        return;
    }

    if (req.files == null || req.files == undefined) {
        res.status(500).json({ error: `${senderName} - Image uploads not found.` });
        return;
    }
    else if (req.files.length == 0) {
        res.status(500).json({ error: `${senderName} - No images sent.` });
        return;
    }
    else {
        res.status(200).json({ success: `${senderName} - ${req.files.length} images saved.` });
        return;
    }
});

module.exports = app;
