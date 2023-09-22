const express = require('express');
const app = express();
const upload = require('./helpers/multer_config').upload;

app.use(express.json());

app.get('/', (req, res, next) => {
    res.status(200).json({ success: 'Hello Server' });
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
