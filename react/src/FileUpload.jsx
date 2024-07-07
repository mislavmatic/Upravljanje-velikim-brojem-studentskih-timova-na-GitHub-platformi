import React, { useState } from 'react';
import "./FileUpload.css"

function FileUpload() {
    const [selectedFile, setSelectedFile] = useState();
    // const [fileName, setFileName] = useState('');

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        setSelectedFile(file);
        // setFileName(file ? file.name : '');
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!selectedFile) {
            alert('No file selected!');
            return;
        }
    
        const fileExtension = selectedFile.name.split('.').pop().toLowerCase();
        if (fileExtension !== 'xls' && fileExtension !== 'xlsx') {
            alert('Please select an Excel file (.xls or .xlsx)');
            return;
        }
    
        const formData = new FormData();
        formData.append('file', selectedFile);
    
        fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.text())
        .then(message => alert(message))
        .catch(error => console.error(error));
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* <label htmlFor="input_file" className="custom-file-upload">
                {fileName}
            </label> */}
            <input type="file" id='input_file' onChange={handleFileChange}/>
            <button type="submit">Submit</button>
        </form>
    );
}

export default FileUpload;