/**
 * Created by lenovo on 2017/12/23.
 */
$(function(){
    var error_name = true;
    var error_pwd = true;
    var error_cpwd = true;
    var error_email = true;
    var error_check = false;

    // 检查用户名合法性
    $('#user_name').blur(function(){
        check_user_name();
    });

    $('#pwd').blur(function(){
        check_pwd();
    });

    $('#cpwd').blur(function(){
       check_cpwd();
    });

    $('#email').blur(function(){
       check_email();
    });

    $('#allow').click(function(){
       if($(this).is(':checked'))
       {
           error_check = false;
           $(this).siblings('span').hide();
       }
       else
       {
           error_check = true;
           $(this).siblings('span').html('请勾选同意').show();
       }
    });

    //检查密码的合法性
    function check_user_name(){
        var len = $('#user_name').val().length;
        if(len<5||len>20){
            $('#user_name').next().html('请输入5-20个字符的用户名').show();
            error_name = true;
        }
        else
        {
            //
            //  '/user/register_valid/',{'uname':$('#user_name').val()}
            $.get('/user/register_valid/',{'uname':$('#user_name').val()}, function(data){
                if(data.valid>=1)
                {
                    $('#user_name').next().html('用户名已经存在').show();
                    error_name = true;
                }else{
                    $('#user_name').next().hide();
                    error_name = false;
                }
            });
            $('#user_name').next().hide();
            error_name = false;
        }
    }

    function check_pwd(){
        var len = $('#pwd').val().length;
        if(len<8||len>20)
        {
            $('#pwd').next().html('密码最少8位，最长20位').show();
            error_pwd = true;
        }
        else{
            $('#pwd').next().hide();
            error_pwd =false;
        }
    }

    function check_cpwd(){
        var pass = $('#pwd').val();
        var cpass = $('#cpwd').val();
        if(pass!=cpass)
        {
            $('#cpwd').next().html('两次输入的密码不一致').show();
            error_pwd = true;
        }
        else
        {
            $('#cpwd').next().hide();
            error_cpwd = false;
        }
    }

    function check_email(){
        var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
        if(re.test($('#email').val()))
        {
            $('#email').next().hide;
            error_email = false;
        }
        else{
            $('#email').next().html('你输入的邮箱格式不正确').show();
            error_email = true
        }
    }

    $('#reg_form').submit(function()
    {
        check_user_name();
        check_pwd();
        check_cpwd();
        check_email();

        if(error_name == false && error_pwd == false && error_cpwd == false && error_email==false && error_check == false)
        {
            return true;
        }
        else
        {
            return false;
        }
    })

});


