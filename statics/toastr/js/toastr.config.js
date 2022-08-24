toastr.options = { 
    // toastr配置
    "closeButton": false, //是否显示关闭按钮
    "debug": false, //是否使用debug模式
    "progressBar": false, //是否显示进度条，当为false时候不显示；当为true时候，显示进度条，当进度条缩短到0时候，消息通知弹窗消失
    "positionClass": "toast-top-center",//显示的动画位置
    "showDuration": "400", //显示的动画时间
    "hideDuration": "1000", //消失的动画时间
    "timeOut": "30000", //展现时间
    "extendedTimeOut": "1000", //设置当你鼠标滑入后的timeout，该timeout会更新关闭所需的timeout.
    "showEasing": "swing", //显示时的动画缓冲方式
    "hideEasing": "linear", //消失时的动画缓冲方式
    "showMethod": "fadeIn", //显示时的动画方式
    "hideMethod": "fadeOut", //消失时的动画方式
    "newestOnTop": true, // 新的toastr会显示在旧的toastr前面
    "preventDuplicates": true, // 重复内容的提示框只出现一次，无论提示框是打开还是关闭
    "preventOpenDuplicates": true, //重复内容的提示框在开启时只出现一个 如果当前的提示框已经打开，不会多开。直到提示框关闭后，才可再开
    "maxOpened": 1, //页面一次性最多显示多少个toastr
    "allowHtml": false, // 设置提示内容可包含html格式
    "closeButton": false,//设置显示"X" 关闭按钮
    "closeHtml": '<button>x</button>',
    "iconClasses": {    //设置各个类型的icon图标class
        "error": 'toast-error',
        "info": 'toast-info',
        "success": 'toast-success',
        "warning": 'toast-warning'
    }, 
    "messageClass": 'toast-message',    // 设置toastr提示信息的class
    "tapToDismiss": true,   // 设置被点击是否关闭
    "templates": {      // 自定义模板
        "toast": 'directives/toast/toast.html',
        "progressbar": 'directives/progressbar/progressbar.html'
    },
    "titleClass": 'toast-title',    // 设置toastr标题的class
    "toastClass": 'toast'       // 设置toastr基本的class
}