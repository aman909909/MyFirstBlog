$("#cl").click(function(){
    $("#cl").text("Hello world!");
  });

$('.btt').mouseenter(function(){
    $(this).delay(10000).css("text-decoration","underline");
});
$('.btt').mouseleave(function(){
    $(this).delay(200).css("text-decoration","none");
});
$('h1').mouseenter(function(){
    $('h1').delay(1000).css("color","#595959");
});
$('h1').mouseleave(function(){
    $('h1').css("color","white");
});
setInterval(
    function () {
      var randomColor = Math.floor(Math.random()*16777215).toString(16);
      var cc=document.getElementById('man');
      man.style.backgroundColor = "#"+randomColor;
    
    },1000);

    $(document).ready(function () {
        $('.nav li a').click(function(e) {
    
            $('.nav li.active').removeClass('active');
    
            var $parent = $(this).parent();
            $parent.addClass('active');
            e.preventDefault();
        });
    });