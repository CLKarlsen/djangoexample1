$(document).ready(function(){

    $(".add-points-link").click(function(event) {
        event.preventDefault();
        var note_id = $(this).data("noteid");
        alert("hei " + note_id);
    });


    $("#increase_passed_exams_button").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: $('#passed_exams_url').val()
        })
        .done(function(data){
            var passed_exams_updated = data['passed_exams_updated'];
            $("#passed_exams_cell").html(passed_exams_updated);
        });
    });

    $("#increase_number_of_courses_button").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: $('#increase_number_of_courses_url').val()
        })
        .done(function(data){
            var number_of_courses_updated = data['number_of_courses_updated'];
            $("#number_of_courses_cell").html(number_of_courses_updated);
        });
    });

    $("#decrease_number_of_courses_button").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: $('#decrease_number_of_courses_url').val()
        })
        .done(function(data){
            var number_of_courses_updated = data['number_of_courses_updated'];
            $("#number_of_courses_cell").html(number_of_courses_updated);
        });
    });








});

