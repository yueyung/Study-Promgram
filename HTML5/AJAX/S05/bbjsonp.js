$(document).ready(function(){
    $.ajax({
    type:"GET",
    url:"https://10.3.74.189/ajax/bb.php",
    dataType:"jsonp",
    jsonp:"callback",
    success:function(data){
      console.log(data);
      $('#result').html("返回的数据结果："+data.msg);
    },
    error:function(jqXHR){
      console.log(jqXHR.status);
      alert("失败");
    }
  });
});