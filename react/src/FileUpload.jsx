import React, { useState } from 'react';

function FileUpload() {
    const [selectedFile, setSelectedFile] = useState();

    const handleFileChange = (e) => {
        setSelectedFile(e.target.files[0]);
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
            <input type="file" onChange={handleFileChange} />
            <button type="submit">Submit</button>
        </form>
    );
}

export default FileUpload;