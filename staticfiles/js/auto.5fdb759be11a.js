/*var sound = document.createElement('audio')
    sound.id = 'audio'
    sound.controls = 'controls'
    sound.src = 'https://www.youtube.com/watch?v=MwTcBIqkrsI'
    sound.type = 'audio/mp3'
    document.body.appendChild(sound)

    function playAudio() {
      document.getElementById('audio').play();
    }

    setTimeout("playAudio()", 3000);*/
    function openForm() {
      document.getElementById("myForm").style.display = "block";
    }

    function closeForm() {
      document.getElementById("myForm").style.display = "none";
    }
   $(document).ready(function() {
      function showLoading() {
        $("#loading").show();
      }

      function hideLoading() {
        $("#loading").hide();
      }

    hideLoading();
    $(function(){
     var $newChat = $('#newChatForm');
     
     var $newChatForm = $('#newChatForm')
     $newChatForm.on('submit', function(e){
      e.preventDefault();
      var newText = $('#pubchat').val();
      $('#output').text(newText).show();
      $('#output').addClass('card text-center btn btn-secondary')
      
      $('#pubchat').val('');
      showLoading();
     })
  })
  
  })