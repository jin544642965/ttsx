/**
 * Created by lenovo on 2017/12/29.
 */

$(function(){
    var name_ok = true
    var pass_ok = true
    //var qq = {{ name_error }};
    //alert(qq);
    if('{{name_error}}' == '1'){
        $('.user_error').html("用户名错误").show();
        name_ok = false;
        console.log("cccc");
    }else{
        console.log("dddd");
    }

    if("{{pwd_error}}" == "1"){
        $('.pwd_error').html("密码错误").show();
        pass_ok = false;
        console.log("bbb");
    }else{
        console.log("aaa");
    }


    $('.name_input').blur(function(){
        var len =$(this).val().length;
        if(len<5||len>20)
        {
            $('.user_error').html("请输入5-20个字符的用户名").show();
            name_ok = false;
        }else{
            $('.user_error').html("").hide();
            name_ok = true;
        }
    });

    $('.pass_input').blur(function(){
        var len = $(this).val().length;
        if(len<8||len>20)
        {

            $('.pwd_error').html("密码最少为8位最长20位").show();
            pass_ok= false;
        }else
        {
            $('.pwd_error').html("").hide();
            pass_ok= true;
        }
    });

    $('form').submit(function(){
        $('.name_input').blur();
        $('.pass_input').blur();
        return name_ok && pass_ok;
    });


});