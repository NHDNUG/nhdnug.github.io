; window.nhdnug = window.nhdnug || {};
(function(window, document, $, nhdnug, undefined){
    var $raffleFillerMessage = $("#raffleFillerMessage"),
        $raffleSpinner = $("#raffleSpinner"),
        $rafflePicks = $("#rafflePicks"),
        $rangeStart = $("#rangeStart"),
        $rangeEnd = $("#rangeEnd"),
        $resetButton = $("#resetButton"),
        $drawButton = $("#drawButton"),
        $formError = $("#formError");
        
    var choices = null,
        numChoices = 0,
        numPicks = 0;
    
    // polyfill for Number.isInteger (IE needs this)    
    Number.isInteger = Number.isInteger || function(value) {
        return typeof value === "number" && 
            isFinite(value) && 
            Math.floor(value) === value;
    };
        
    
    var toggleRaffleState = function(state) {
      if (state) {
          $raffleFillerMessage.hide();
          $raffleSpinner.show();
          $rangeStart.prop('disabled', true);
          $rangeEnd.prop('disabled', true);
      } else {
          $raffleSpinner.hide();
          $raffleFillerMessage.show();
          $rangeStart.prop('disabled', false);
          $rangeEnd.prop('disabled', false);
          choices = null;
          $rafflePicks.empty();
          numChoices = 0;
          numPicks = 0;
          clearError();
      }
    };
    
    var checkInputCondition = function() {
        var rangeStart = +$rangeStart.val(),
            rangeEnd = +$rangeEnd.val();
            
        if (!Number.isInteger(rangeStart) || !Number.isInteger(rangeEnd)) {
            showError('Range Start and Range End must be whole numbers.');
            return false;
        } else if (rangeStart === '' || rangeEnd === '') {
            showError('Range Start and Range End are required.');
            return false;
        } else if (rangeStart < 1) {
            showError('Range Start must be a positive number.');
            return false;
        } else if (rangeStart > rangeEnd || rangeStart == rangeEnd) {
            showError('Range Start must be less than Range End');
            return false;
        }
        clearError();
        return true;
    };
    
    var initRaffle = function() {
        var rangeStart = parseInt($rangeStart.val()),
            rangeEnd = parseInt($rangeEnd.val());
            
        choices = [];
        
        var numChoices = (rangeEnd - rangeStart + 1);
        for(var i = rangeStart; i < (rangeEnd+1); i++) {
            choices.push({pick: i, available: true});
        }
        
        return numChoices;
    };
    
    var getChoice = function() {
        var gotChoice = false;
        var rNum, choice, pick;
        while(!gotChoice) {
            rNum = Math.floor(Math.random() * numChoices);
            choice = choices[rNum];
            if (choice.available) {     
                pick = choice.pick;       
                gotChoice = true;
                choice.available = false;
                numPicks++;
            }
        }
        return pick;
    };
    
    var raffle = function() {
        if (choices === null) {
            numChoices = initRaffle();            
        } else if (numPicks === numChoices) {
            alert('All numbers have been picked!');
            return;
        }
        
        var choice = getChoice();
        $raffleSpinner.text(choice);
        $rafflePicks.prepend("<li class='list-group-item'>" + choice + "</li>");
         
    };
    var showError = function(msg) {
        $formError.text(msg).show();
    };
    var clearError = function() {
        $formError.hide();
    };
    
    // attach events
    $drawButton.click(function(){
        if (checkInputCondition()) {
            toggleRaffleState(true);
            raffle();    
        } 
        return false;
    });
    $resetButton.click(function(){
        toggleRaffleState(false);
        
        return false;
    });
})(window, document, jQuery, window.nhdnug);