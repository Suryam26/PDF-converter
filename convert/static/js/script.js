$(document).ready(function () { 

    $('input[type="file"]').change(function(e) { 
        let fileName = e.target.files[0].name;
        $("#fileName").html(fileName); 
        if (fileName.substr(fileName.length - 4) == ".pdf") {
            $("#fileName").css("color", "green");
            $("#uploadButton").prop('disabled', false);
        }
        else {
            $("#fileName").css("color", "red");
            $("#uploadButton").prop('disabled', true);    
        }
    }); 

    $('select').change(function(e) { 
        let value = $('select').find(":selected").val();
        if (value == "None") {
            $("#convertButton").prop('disabled', true);
        }
        else {
            $("#convertButton").prop('disabled', false);    
        }
    }); 

    var selector = `option[value="${ $('#selected').html() }"]`
    $(selector).prop('selected','selected')
});
         