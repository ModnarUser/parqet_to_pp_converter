document.addEventListener('DOMContentLoaded', function() {
    var convertButton = document.getElementById('convert-button');
    var fileInput = document.getElementById('file-upload');
    var form = document.querySelector('.upload-form');

    fileInput.addEventListener('change', function() {
        var fileName = this.value.split('\\').pop();
        document.querySelector('.file-label').textContent = fileName ? fileName : 'Choose a file';
    });

    form.addEventListener('submit', function(event) {
        if (fileInput.value) {
            convertButton.textContent = 'Converting...';
            convertButton.disabled = true;

            var checkDownloadCookie = setInterval(function() {
                if (document.cookie.indexOf('fileDownload=true') != -1) {
                    // Clear the cookie and update button text
                    document.cookie = 'fileDownload=; Max-Age=-99999999;';  
                    convertButton.textContent = 'Done';
                    clearInterval(checkDownloadCookie);
                }
            }, 1000); // Check every second
        } else {
            event.preventDefault(); // Prevent form submission if no file is selected
            alert('Please select a file to convert.');
        }
    });
});
