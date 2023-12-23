document.getElementById('file-upload').addEventListener('change', function() {
    var fileName = this.value.split('\\').pop();
    document.querySelector('.file-label').textContent = fileName ? fileName : 'Choose a file';
});
document.addEventListener('DOMContentLoaded', function() {
    var convertButton = document.getElementById('convert-button');
    var fileInput = document.getElementById('file-upload');

    convertButton.addEventListener('click', function() {
        if (fileInput.value) {
            // Change button text to 'Converting...' when clicked
            convertButton.textContent = 'Converting...';
        } else {
            alert('Please select a file to convert.');
        }
    });

    // Check for a download event
    document.addEventListener('click', function(event) {
        if (event.target && event.target.tagName === 'A' && event.target.download) {
            // Change button text to 'Done' when download starts
            convertButton.textContent = 'Done';
            convertButton.disabled = true;
        }
    });
});