$('#fileType').change(function (e) { 
    let fileName = $('#uploadButton')[0].files[0].name;
    let fileType = $("#fileType option:selected").val();
    let newName = fileName.slice(0, -4) + fileType;
    $("#downloadButton").attr("href", newName);
    });