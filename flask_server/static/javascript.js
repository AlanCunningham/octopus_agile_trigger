document.addEventListener('DOMContentLoaded', function() {
    // Date pickers. We initialise them separetely so we can give them
    // different default values
    var startDateElems = document.querySelectorAll('.datepicker-start');
    var startDateOptions = {
        "format": "ddd dd mmm yyyy",
        "firstDay": 1
    }
    var startDateinstances = M.Datepicker.init(startDateElems, startDateOptions);

    var endDateElems = document.querySelectorAll('.datepicker-end');
    var endDateOptions = {
        "format": "ddd dd mmm yyyy",
        "firstDay": 1
    }
    var endDateinstances = M.Datepicker.init(endDateElems, endDateOptions);

    // Time picker
    var startTimeElems = document.querySelectorAll('.timepicker-start');
    var startTimeOptions = {
        "twelveHour": false,
    }
    var startInstances = M.Timepicker.init(startTimeElems, startTimeOptions);

    var endTimeElems = document.querySelectorAll('.timepicker-end');
    var endTimeOptions = {
        "twelveHour": false,
    }
    var endInstances = M.Timepicker.init(endTimeElems, endTimeOptions);

    // Toggle the sections based on whether we're using the threshold or timer
    const checkbox = document.getElementById('useTimer');
    if (checkbox.checked) {
        document.getElementById("charging-timer").style.display = "";
        document.getElementById("charging-threshold").style.display = "none";
    } else {
        document.getElementById("charging-timer").style.display = "none";
        document.getElementById("charging-threshold").style.display = "";
    }

    // Listener for checkbox
    checkbox.addEventListener('change', (event) => {
      if (event.currentTarget.checked) {
        document.getElementById("charging-timer").style.display = "";
        document.getElementById("charging-threshold").style.display = "none";
      } else {
        document.getElementById("charging-timer").style.display = "none";
        document.getElementById("charging-threshold").style.display = "";
      }
    });

  });