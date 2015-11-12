<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<meta content='IE=edge' http-equiv='X-UA-Compatible'>
<meta content='GitLab Enterprise Edition' name='description'>
<meta content='origin-when-cross-origin' name='referrer'>
<title>project/statics/js/JavaS.js | master | ElmosDS / Judge93 | GitLab</title>
<link href="/assets/favicon-5738a6efe01f3282080df5f467da72a9.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<link href="/assets/application-6e45da8428d567a21d5b1e9422a44651.css" media="all" rel="stylesheet" />
<link href="/assets/print-47fe51cdf70398e5e54b544e0f5cc718.css" media="print" rel="stylesheet" />
<script src="/assets/application-478a3b9da05266815225b23b6f203fb7.js"></script>
<meta content="authenticity_token" name="csrf-param" />
<meta content="MVzxIXMW7d4y5H5EiCq3SxApW5BWt9ksqzyuxXnuDaU=" name="csrf-token" />
<script type="text/javascript">
//<![CDATA[
window.gon={};gon.api_version="v3";gon.default_avatar_url="https://gitlab.com/assets/no_avatar-0b64d25ac5f63e6f0caee99e819105ba.png";gon.default_issues_tracker="gitlab";gon.max_file_size=10;gon.relative_url_root="";gon.user_color_scheme="white";gon.current_user_id=295625;gon.api_token="v9DvKwkCxRXB7QCicV1F";
//]]>
</script>
<meta content='width=device-width, initial-scale=1, maximum-scale=1' name='viewport'>
<meta content='#474D57' name='theme-color'>
<link href="/assets/touch-icon-iphone-4c0496ac9f88e7961644c66b289a6614.png" rel="apple-touch-icon" type="image/vnd.microsoft.icon" />
<link href="/assets/touch-icon-ipad-d64abe7a8e8be6e02245d2ed79da6ff9.png" rel="apple-touch-icon" sizes="76x76" type="image/vnd.microsoft.icon" />
<link href="/assets/touch-icon-iphone-retina-54af16810ab006406b4df81f8a92fe8d.png" rel="apple-touch-icon" sizes="120x120" type="image/vnd.microsoft.icon" />
<link href="/assets/touch-icon-ipad-retina-72774a950890a9e3811ab91f186cc11f.png" rel="apple-touch-icon" sizes="152x152" type="image/vnd.microsoft.icon" />
<meta content='/assets/msapplication-tile-0cf7066c37c04d40809fdcc2bf53a754.png' name='msapplication-TileImage'>
<meta content='#30353E' name='msapplication-TileColor'>

<script>
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-37019925-1']);
  _gaq.push(['_trackPageview']);
  
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>



<style>
  [data-user-is] {
    display: none !important;
  }
  
  [data-user-is="295625"] {
    display: block !important;
  }
  
  [data-user-is="295625"][data-display="inline"] {
    display: inline !important;
  }
  
  [data-user-is-not] {
    display: block !important;
  }
  
  [data-user-is-not][data-display="inline"] {
    display: inline !important;
  }
  
  [data-user-is-not="295625"] {
    display: none !important;
  }
</style>

</head>

<body class='ui_charcoal' data-page='projects:blob:show'>
<script>
  window.project_uploads_path = "/ElmosDS/Judge93/uploads";
  window.markdown_preview_path = "/ElmosDS/Judge93/markdown_preview";
</script>

<header class='header-expanded navbar navbar-fixed-top navbar-gitlab'>
<div class='container-fluid'>
<div class='header-content'>
<button class='navbar-toggle' type='button'>
<span class='sr-only'>Toggle navigation</span>
<i class="fa fa-bars"></i>
</button>
<div class='navbar-collapse collapse'>
<ul class='nav navbar-nav pull-right'>
<li class='hidden-sm hidden-xs'>
<div class='search'>
<form accept-charset="UTF-8" action="/search" class="navbar-form pull-left" method="get"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<input class="search-input form-control" id="search" name="search" placeholder="Search in this project" spellcheck="false" type="search" />
<input id="group_id" name="group_id" type="hidden" />
<input id="project_id" name="project_id" type="hidden" value="566001" />
<input id="search_code" name="search_code" type="hidden" value="true" />
<input id="repository_ref" name="repository_ref" type="hidden" value="master" />

<div class='search-autocomplete-opts hide' data-autocomplete-path='/search/autocomplete' data-autocomplete-project-id='566001' data-autocomplete-project-ref='master'></div>
</form>

</div>
<script>
  $('.search-input').on('keyup', function(e) {
    if (e.keyCode == 27) {
      $('.search-input').blur()
    }
  })
</script>

</li>
<li class='visible-sm visible-xs'>
<a data-placement="bottom" data-toggle="tooltip" href="/search" title="Search"><i class="fa fa-search"></i>
</a></li>
<li>
<a data-placement="bottom" data-toggle="tooltip" href="/projects/new" title="New project"><i class="fa fa-plus fa-fw"></i>
</a></li>
<li>
<a class="logout" data-method="delete" data-placement="bottom" data-toggle="tooltip" href="/users/sign_out" rel="nofollow" title="Sign out"><i class="fa fa-sign-out"></i>
</a></li>
</ul>
</div>
<h1 class='title'><span><a href="/groups/ElmosDS">ElmosDS</a> / <a href="/ElmosDS/Judge93">Judge93</a> &middot; <a href="/ElmosDS/Judge93/tree/master">Files</a></span></h1>
</div>
</div>
</header>


<div class='page-sidebar-expanded page-with-sidebar'>

<div class='sidebar-wrapper nicescroll'>
<div class='header-logo'>
<a class="home" data-placement="bottom" data-toggle="tooltip" href="/" id="js-shortcuts-home" title="Dashboard"><svg width="36px" height="36px" viewBox="0 0 210 210" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="tanuki-logo">
    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
        <g id="logo" sketch:type="MSLayerGroup" transform="translate(0.000000, 10.000000)">
            <g id="Page-1" sketch:type="MSShapeGroup">
                <g id="Fill-1-+-Group-24">
                    <g id="Group-24">
                        <g id="Group">
                            <path d="M105.0614,193.655 L105.0614,193.655 L143.7014,74.734 L66.4214,74.734 L105.0614,193.655 L105.0614,193.655 Z" id="Fill-4" fill="#E24329" class="tanuki-shape"></path>
                            <path d="M105.0614,193.6548 L66.4214,74.7338 L12.2684,74.7338 L105.0614,193.6548 L105.0614,193.6548 Z" id="Fill-8" fill="#FC6D26" class="tanuki-shape"></path>
                            <path d="M12.2685,74.7341 L12.2685,74.7341 L0.5265,110.8731 C-0.5445,114.1691 0.6285,117.7801 3.4325,119.8171 L105.0615,193.6551 L12.2685,74.7341 L12.2685,74.7341 Z" id="Fill-12" fill="#FCA326" class="tanuki-shape"></path>
                            <path d="M12.2685,74.7342 L66.4215,74.7342 L43.1485,3.1092 C41.9515,-0.5768 36.7375,-0.5758 35.5405,3.1092 L12.2685,74.7342 L12.2685,74.7342 Z" id="Fill-16" fill="#E24329" class="tanuki-shape"></path>
                            <path d="M105.0614,193.6548 L143.7014,74.7338 L197.8544,74.7338 L105.0614,193.6548 L105.0614,193.6548 Z" id="Fill-18" fill="#FC6D26" class="tanuki-shape"></path>
                            <path d="M197.8544,74.7341 L197.8544,74.7341 L209.5964,110.8731 C210.6674,114.1691 209.4944,117.7801 206.6904,119.8171 L105.0614,193.6551 L197.8544,74.7341 L197.8544,74.7341 Z" id="Fill-20" fill="#FCA326" class="tanuki-shape"></path>
                            <path d="M197.8544,74.7342 L143.7014,74.7342 L166.9744,3.1092 C168.1714,-0.5768 173.3854,-0.5758 174.5824,3.1092 L197.8544,74.7342 L197.8544,74.7342 Z" id="Fill-22" fill="#E24329" class="tanuki-shape"></path>
                        </g>
                    </g>
                </g>
            </g>
        </g>
    </g>
</svg>

<div class='gitlab-text-container'>
<h3>GitLab</h3>
</div>
</a></div>
<ul class='nav nav-sidebar'>
<li class=""><a class="back-link" data-placement="right" href="/groups/ElmosDS" title="Back to group"><i class="fa fa-caret-square-o-left fa-fw"></i>
<span>
Back to group
</span>
</a></li><li class='separate-item'></li>
<li class="home"><a class="shortcuts-project" data-placement="right" href="/ElmosDS/Judge93" title="Project"><i class="fa fa-home fa-fw"></i>
<span>
Project
</span>
</a></li><li class=""><a class="shortcuts-project-activity" data-placement="right" href="/ElmosDS/Judge93/activity" title="Project Activity"><i class="fa fa-dashboard fa-fw"></i>
<span>
Activity
</span>
</a></li><li class="active"><a class="shortcuts-tree" data-placement="right" href="/ElmosDS/Judge93/tree/master" title="Files"><i class="fa fa-files-o fa-fw"></i>
<span>
Files
</span>
</a></li><li class=""><a class="shortcuts-commits" data-placement="right" href="/ElmosDS/Judge93/commits/master" title="Commits"><i class="fa fa-history fa-fw"></i>
<span>
Commits
</span>
</a></li><li class=""><a class="shortcuts-network" data-placement="right" href="/ElmosDS/Judge93/network/master" title="Network"><i class="fa fa-code-fork fa-fw"></i>
<span>
Network
</span>
</a></li><li class=""><a class="shortcuts-graphs" data-placement="right" href="/ElmosDS/Judge93/graphs/master" title="Graphs"><i class="fa fa-area-chart fa-fw"></i>
<span>
Graphs
</span>
</a></li><li class=""><a data-placement="right" href="/ElmosDS/Judge93/milestones" title="Milestones"><i class="fa fa-clock-o fa-fw"></i>
<span>
Milestones
</span>
</a></li><li class=""><a class="shortcuts-issues" data-placement="right" href="/ElmosDS/Judge93/issues" title="Issues"><i class="fa fa-exclamation-circle fa-fw"></i>
<span>
Issues
<span class='count issue_counter'>17</span>
</span>
</a></li><li class=""><a class="shortcuts-merge_requests" data-placement="right" href="/ElmosDS/Judge93/merge_requests" title="Merge Requests"><i class="fa fa-tasks fa-fw"></i>
<span>
Merge Requests
<span class='count merge_counter'>2</span>
</span>
</a></li><li class=""><a data-placement="right" href="/ElmosDS/Judge93/labels" title="Labels"><i class="fa fa-tags fa-fw"></i>
<span>
Labels
</span>
</a></li><li class=""><a class="shortcuts-wiki" data-placement="right" href="/ElmosDS/Judge93/wikis/home" title="Wiki"><i class="fa fa-book fa-fw"></i>
<span>
Wiki
</span>
</a></li></ul>

<div class='collapse-nav'>
<a class="toggle-nav-collapse" href="#" title="Open/Close"><i class="fa fa-angle-left"></i></a>

</div>
<a class="sidebar-user" href="/u/sina-khorami"><img alt="User activity" class="avatar avatar s36" src="https://secure.gravatar.com/avatar/2e148aaae94520e39b5404940bfbf89f?s=60&amp;d=identicon" />
<div class='username'>
sina-khorami
</div>
</a></div>
<div class='content-wrapper'>
<div class='flash-container'>
</div>


<div class='container-fluid container-limited'>
<div class='content'>
<div class='clearfix'>


<div class='tree-ref-holder'>
<form accept-charset="UTF-8" action="/ElmosDS/Judge93/refs/switch" class="project-refs-form" method="get"><div style="display:none"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<select class="project-refs-select select2 select2-sm" id="ref" name="ref"><optgroup label="Branches"><option selected="selected" value="master">master</option></optgroup><optgroup label="Tags"></optgroup></select>
<input id="destination" name="destination" type="hidden" value="blob" />
<input id="path" name="path" type="hidden" value="project/statics/js/JavaS.js" />
</form>


</div>
<div class='tree-holder' id='tree-holder'>
<ul class='breadcrumb repo-breadcrumb'>
<li>
<i class='fa fa-angle-right'></i>
<a href="/ElmosDS/Judge93/tree/master">Judge93
</a></li>
<li>
<a href="/ElmosDS/Judge93/tree/master/project">project</a>
</li>
<li>
<a href="/ElmosDS/Judge93/tree/master/project/statics">statics</a>
</li>
<li>
<a href="/ElmosDS/Judge93/tree/master/project/statics/js">js</a>
</li>
<li>
<a href="/ElmosDS/Judge93/blob/master/project/statics/js/JavaS.js"><strong>
JavaS.js
</strong>
</a></li>
</ul>
<ul class='blob-commit-info hidden-xs'>
<li class='commit js-toggle-container'>
<div class='commit-row-title'>
<strong class='str-truncated'>
<a class="commit-row-message" href="/ElmosDS/Judge93/commit/c5ea8c8c525b3bf5e5fb54c383fa0a9cdfcd0a24">user profile updated</a>
</strong>
<div class='pull-right'>
<a class="commit_short_id" href="/ElmosDS/Judge93/commit/c5ea8c8c525b3bf5e5fb54c383fa0a9cdfcd0a24">c5ea8c8c</a>
</div>
<div class='notes_count'>
</div>
</div>
<div class='commit-row-info'>
<a class="commit-author-link has_tooltip" data-original-title="talayeh.riahi@gmail.com" href="/u/talayeh_R"><img alt="" class="avatar s24" src="https://secure.gravatar.com/avatar/f0565dc4587a3e6dcc95f17486c55203?s=24&amp;d=identicon" width="24" /> <span class="commit-author-name">talayeh</span></a>
authored
<div class='committed_ago'>
<time class="time_ago js-timeago" data-container="body" data-placement="top" data-toggle="tooltip" datetime="2015-11-12T13:18:26Z" title="Nov 12, 2015 1:18pm">2015-11-12 16:48:26 +0330</time> &nbsp;
</div>
<a class="pull-right" href="/ElmosDS/Judge93/tree/c5ea8c8c525b3bf5e5fb54c383fa0a9cdfcd0a24">Browse Code »</a>
</div>
</li>

</ul>
<div class='blob-content-holder' id='blob-content-holder'>
<article class='file-holder'>
<div class='file-title'>
<i class="fa fa-file-text-o fa-fw"></i>
<strong>
JavaS.js
</strong>
<small>
3.61 KB
</small>
<div class='file-actions hidden-xs'>
<div class='btn-group tree-btn-group'>
<span class="btn btn-small disabled">Edit</span>
<a class="btn btn-sm" href="/ElmosDS/Judge93/raw/master/project/statics/js/JavaS.js" target="_blank">Raw</a>
<a class="btn btn-sm" href="/ElmosDS/Judge93/blame/master/project/statics/js/JavaS.js">Blame</a>
<a class="btn btn-sm" href="/ElmosDS/Judge93/commits/master/project/statics/js/JavaS.js">History</a>
<a class="btn btn-sm" href="/ElmosDS/Judge93/blob/601a7e0cbe1c5a6eddea70ae792630b8de18e50e/project/statics/js/JavaS.js">Permalink</a>
</div>

</div>
</div>
<div class='file-content code'>
<div class='code file-content js-syntax-highlight white'>
<div class='line-numbers'>
<a data-line-number='1' href='#L1' id='L1'>
<i class='fa fa-link'></i>
1
</a>
<a data-line-number='2' href='#L2' id='L2'>
<i class='fa fa-link'></i>
2
</a>
<a data-line-number='3' href='#L3' id='L3'>
<i class='fa fa-link'></i>
3
</a>
<a data-line-number='4' href='#L4' id='L4'>
<i class='fa fa-link'></i>
4
</a>
<a data-line-number='5' href='#L5' id='L5'>
<i class='fa fa-link'></i>
5
</a>
<a data-line-number='6' href='#L6' id='L6'>
<i class='fa fa-link'></i>
6
</a>
<a data-line-number='7' href='#L7' id='L7'>
<i class='fa fa-link'></i>
7
</a>
<a data-line-number='8' href='#L8' id='L8'>
<i class='fa fa-link'></i>
8
</a>
<a data-line-number='9' href='#L9' id='L9'>
<i class='fa fa-link'></i>
9
</a>
<a data-line-number='10' href='#L10' id='L10'>
<i class='fa fa-link'></i>
10
</a>
<a data-line-number='11' href='#L11' id='L11'>
<i class='fa fa-link'></i>
11
</a>
<a data-line-number='12' href='#L12' id='L12'>
<i class='fa fa-link'></i>
12
</a>
<a data-line-number='13' href='#L13' id='L13'>
<i class='fa fa-link'></i>
13
</a>
<a data-line-number='14' href='#L14' id='L14'>
<i class='fa fa-link'></i>
14
</a>
<a data-line-number='15' href='#L15' id='L15'>
<i class='fa fa-link'></i>
15
</a>
<a data-line-number='16' href='#L16' id='L16'>
<i class='fa fa-link'></i>
16
</a>
<a data-line-number='17' href='#L17' id='L17'>
<i class='fa fa-link'></i>
17
</a>
<a data-line-number='18' href='#L18' id='L18'>
<i class='fa fa-link'></i>
18
</a>
<a data-line-number='19' href='#L19' id='L19'>
<i class='fa fa-link'></i>
19
</a>
<a data-line-number='20' href='#L20' id='L20'>
<i class='fa fa-link'></i>
20
</a>
<a data-line-number='21' href='#L21' id='L21'>
<i class='fa fa-link'></i>
21
</a>
<a data-line-number='22' href='#L22' id='L22'>
<i class='fa fa-link'></i>
22
</a>
<a data-line-number='23' href='#L23' id='L23'>
<i class='fa fa-link'></i>
23
</a>
<a data-line-number='24' href='#L24' id='L24'>
<i class='fa fa-link'></i>
24
</a>
<a data-line-number='25' href='#L25' id='L25'>
<i class='fa fa-link'></i>
25
</a>
<a data-line-number='26' href='#L26' id='L26'>
<i class='fa fa-link'></i>
26
</a>
<a data-line-number='27' href='#L27' id='L27'>
<i class='fa fa-link'></i>
27
</a>
<a data-line-number='28' href='#L28' id='L28'>
<i class='fa fa-link'></i>
28
</a>
<a data-line-number='29' href='#L29' id='L29'>
<i class='fa fa-link'></i>
29
</a>
<a data-line-number='30' href='#L30' id='L30'>
<i class='fa fa-link'></i>
30
</a>
<a data-line-number='31' href='#L31' id='L31'>
<i class='fa fa-link'></i>
31
</a>
<a data-line-number='32' href='#L32' id='L32'>
<i class='fa fa-link'></i>
32
</a>
<a data-line-number='33' href='#L33' id='L33'>
<i class='fa fa-link'></i>
33
</a>
<a data-line-number='34' href='#L34' id='L34'>
<i class='fa fa-link'></i>
34
</a>
<a data-line-number='35' href='#L35' id='L35'>
<i class='fa fa-link'></i>
35
</a>
<a data-line-number='36' href='#L36' id='L36'>
<i class='fa fa-link'></i>
36
</a>
<a data-line-number='37' href='#L37' id='L37'>
<i class='fa fa-link'></i>
37
</a>
<a data-line-number='38' href='#L38' id='L38'>
<i class='fa fa-link'></i>
38
</a>
<a data-line-number='39' href='#L39' id='L39'>
<i class='fa fa-link'></i>
39
</a>
<a data-line-number='40' href='#L40' id='L40'>
<i class='fa fa-link'></i>
40
</a>
<a data-line-number='41' href='#L41' id='L41'>
<i class='fa fa-link'></i>
41
</a>
<a data-line-number='42' href='#L42' id='L42'>
<i class='fa fa-link'></i>
42
</a>
<a data-line-number='43' href='#L43' id='L43'>
<i class='fa fa-link'></i>
43
</a>
<a data-line-number='44' href='#L44' id='L44'>
<i class='fa fa-link'></i>
44
</a>
<a data-line-number='45' href='#L45' id='L45'>
<i class='fa fa-link'></i>
45
</a>
<a data-line-number='46' href='#L46' id='L46'>
<i class='fa fa-link'></i>
46
</a>
<a data-line-number='47' href='#L47' id='L47'>
<i class='fa fa-link'></i>
47
</a>
<a data-line-number='48' href='#L48' id='L48'>
<i class='fa fa-link'></i>
48
</a>
<a data-line-number='49' href='#L49' id='L49'>
<i class='fa fa-link'></i>
49
</a>
<a data-line-number='50' href='#L50' id='L50'>
<i class='fa fa-link'></i>
50
</a>
<a data-line-number='51' href='#L51' id='L51'>
<i class='fa fa-link'></i>
51
</a>
<a data-line-number='52' href='#L52' id='L52'>
<i class='fa fa-link'></i>
52
</a>
<a data-line-number='53' href='#L53' id='L53'>
<i class='fa fa-link'></i>
53
</a>
<a data-line-number='54' href='#L54' id='L54'>
<i class='fa fa-link'></i>
54
</a>
<a data-line-number='55' href='#L55' id='L55'>
<i class='fa fa-link'></i>
55
</a>
<a data-line-number='56' href='#L56' id='L56'>
<i class='fa fa-link'></i>
56
</a>
<a data-line-number='57' href='#L57' id='L57'>
<i class='fa fa-link'></i>
57
</a>
<a data-line-number='58' href='#L58' id='L58'>
<i class='fa fa-link'></i>
58
</a>
<a data-line-number='59' href='#L59' id='L59'>
<i class='fa fa-link'></i>
59
</a>
<a data-line-number='60' href='#L60' id='L60'>
<i class='fa fa-link'></i>
60
</a>
<a data-line-number='61' href='#L61' id='L61'>
<i class='fa fa-link'></i>
61
</a>
<a data-line-number='62' href='#L62' id='L62'>
<i class='fa fa-link'></i>
62
</a>
<a data-line-number='63' href='#L63' id='L63'>
<i class='fa fa-link'></i>
63
</a>
<a data-line-number='64' href='#L64' id='L64'>
<i class='fa fa-link'></i>
64
</a>
<a data-line-number='65' href='#L65' id='L65'>
<i class='fa fa-link'></i>
65
</a>
<a data-line-number='66' href='#L66' id='L66'>
<i class='fa fa-link'></i>
66
</a>
<a data-line-number='67' href='#L67' id='L67'>
<i class='fa fa-link'></i>
67
</a>
<a data-line-number='68' href='#L68' id='L68'>
<i class='fa fa-link'></i>
68
</a>
<a data-line-number='69' href='#L69' id='L69'>
<i class='fa fa-link'></i>
69
</a>
<a data-line-number='70' href='#L70' id='L70'>
<i class='fa fa-link'></i>
70
</a>
<a data-line-number='71' href='#L71' id='L71'>
<i class='fa fa-link'></i>
71
</a>
<a data-line-number='72' href='#L72' id='L72'>
<i class='fa fa-link'></i>
72
</a>
<a data-line-number='73' href='#L73' id='L73'>
<i class='fa fa-link'></i>
73
</a>
<a data-line-number='74' href='#L74' id='L74'>
<i class='fa fa-link'></i>
74
</a>
<a data-line-number='75' href='#L75' id='L75'>
<i class='fa fa-link'></i>
75
</a>
<a data-line-number='76' href='#L76' id='L76'>
<i class='fa fa-link'></i>
76
</a>
<a data-line-number='77' href='#L77' id='L77'>
<i class='fa fa-link'></i>
77
</a>
<a data-line-number='78' href='#L78' id='L78'>
<i class='fa fa-link'></i>
78
</a>
<a data-line-number='79' href='#L79' id='L79'>
<i class='fa fa-link'></i>
79
</a>
<a data-line-number='80' href='#L80' id='L80'>
<i class='fa fa-link'></i>
80
</a>
<a data-line-number='81' href='#L81' id='L81'>
<i class='fa fa-link'></i>
81
</a>
<a data-line-number='82' href='#L82' id='L82'>
<i class='fa fa-link'></i>
82
</a>
<a data-line-number='83' href='#L83' id='L83'>
<i class='fa fa-link'></i>
83
</a>
<a data-line-number='84' href='#L84' id='L84'>
<i class='fa fa-link'></i>
84
</a>
<a data-line-number='85' href='#L85' id='L85'>
<i class='fa fa-link'></i>
85
</a>
<a data-line-number='86' href='#L86' id='L86'>
<i class='fa fa-link'></i>
86
</a>
<a data-line-number='87' href='#L87' id='L87'>
<i class='fa fa-link'></i>
87
</a>
<a data-line-number='88' href='#L88' id='L88'>
<i class='fa fa-link'></i>
88
</a>
<a data-line-number='89' href='#L89' id='L89'>
<i class='fa fa-link'></i>
89
</a>
<a data-line-number='90' href='#L90' id='L90'>
<i class='fa fa-link'></i>
90
</a>
<a data-line-number='91' href='#L91' id='L91'>
<i class='fa fa-link'></i>
91
</a>
<a data-line-number='92' href='#L92' id='L92'>
<i class='fa fa-link'></i>
92
</a>
<a data-line-number='93' href='#L93' id='L93'>
<i class='fa fa-link'></i>
93
</a>
<a data-line-number='94' href='#L94' id='L94'>
<i class='fa fa-link'></i>
94
</a>
<a data-line-number='95' href='#L95' id='L95'>
<i class='fa fa-link'></i>
95
</a>
<a data-line-number='96' href='#L96' id='L96'>
<i class='fa fa-link'></i>
96
</a>
<a data-line-number='97' href='#L97' id='L97'>
<i class='fa fa-link'></i>
97
</a>
<a data-line-number='98' href='#L98' id='L98'>
<i class='fa fa-link'></i>
98
</a>
<a data-line-number='99' href='#L99' id='L99'>
<i class='fa fa-link'></i>
99
</a>
<a data-line-number='100' href='#L100' id='L100'>
<i class='fa fa-link'></i>
100
</a>
<a data-line-number='101' href='#L101' id='L101'>
<i class='fa fa-link'></i>
101
</a>
<a data-line-number='102' href='#L102' id='L102'>
<i class='fa fa-link'></i>
102
</a>
<a data-line-number='103' href='#L103' id='L103'>
<i class='fa fa-link'></i>
103
</a>
<a data-line-number='104' href='#L104' id='L104'>
<i class='fa fa-link'></i>
104
</a>
<a data-line-number='105' href='#L105' id='L105'>
<i class='fa fa-link'></i>
105
</a>
<a data-line-number='106' href='#L106' id='L106'>
<i class='fa fa-link'></i>
106
</a>
<a data-line-number='107' href='#L107' id='L107'>
<i class='fa fa-link'></i>
107
</a>
<a data-line-number='108' href='#L108' id='L108'>
<i class='fa fa-link'></i>
108
</a>
<a data-line-number='109' href='#L109' id='L109'>
<i class='fa fa-link'></i>
109
</a>
</div>
<pre class="code highlight"><code><span id="LC1" class="line"></span>&#x000A;<span id="LC2" class="line"><span class="nx">$</span><span class="p">(</span><span class="nb">document</span><span class="p">).</span><span class="nx">ready</span><span class="p">(</span><span class="kd">function</span> <span class="p">()</span> <span class="p">{</span></span>&#x000A;<span id="LC3" class="line"></span>&#x000A;<span id="LC4" class="line"><span class="c1">//show create team</span></span>&#x000A;<span id="LC5" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#team&quot;</span><span class="p">).</span><span class="nx">click</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span></span>&#x000A;<span id="LC6" class="line">        <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.post&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;display&#39;</span><span class="p">,</span> <span class="s1">&#39;none&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC7" class="line">        <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.settingcontent&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;display&#39;</span><span class="p">,</span> <span class="s1">&#39;none&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC8" class="line">        <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#titlePage&#39;</span><span class="p">).</span><span class="nx">html</span><span class="p">(</span><span class="s2">&quot;Team&quot;</span><span class="p">);</span></span>&#x000A;<span id="LC9" class="line">        <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.close-page&#39;</span><span class="p">).</span><span class="nx">removeClass</span><span class="p">(</span><span class="s1">&#39;close-page&#39;</span><span class="p">).</span><span class="nx">addClass</span><span class="p">(</span><span class="s1">&#39;open-page&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC10" class="line">    <span class="p">});</span></span>&#x000A;<span id="LC11" class="line"></span>&#x000A;<span id="LC12" class="line">  <span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#setting&quot;</span><span class="p">).</span><span class="nx">click</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span> </span>&#x000A;<span id="LC13" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#usernameitem&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;background-color&#39;</span><span class="p">,</span> <span class="s1">&#39;#312736&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC14" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#setting&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;background-color&#39;</span><span class="p">,</span> <span class="s1">&#39;#6C6368&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC15" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.post&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;display&#39;</span><span class="p">,</span> <span class="s1">&#39;none&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC16" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.open-page&#39;</span><span class="p">).</span><span class="nx">removeClass</span><span class="p">(</span><span class="s1">&#39;open-page&#39;</span><span class="p">).</span><span class="nx">addClass</span><span class="p">(</span><span class="s1">&#39;close-page&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC17" class="line">      <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#titlePage&#39;</span><span class="p">).</span><span class="nx">html</span><span class="p">(</span><span class="s2">&quot;News&quot;</span><span class="p">);</span></span>&#x000A;<span id="LC18" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.settingcontent&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;display&#39;</span><span class="p">,</span> <span class="s1">&#39;block&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC19" class="line"></span>&#x000A;<span id="LC20" class="line">  <span class="p">});</span></span>&#x000A;<span id="LC21" class="line">  <span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#usernameitem&quot;</span><span class="p">).</span><span class="nx">click</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span> </span>&#x000A;<span id="LC22" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#setting&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;background-color&#39;</span><span class="p">,</span> <span class="s1">&#39;#312736&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC23" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#usernameitem&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;background-color&#39;</span><span class="p">,</span> <span class="s1">&#39;#6C6368&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC24" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.settingcontent&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;display&#39;</span><span class="p">,</span> <span class="s1">&#39;none&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC25" class="line">      <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.open-page&#39;</span><span class="p">).</span><span class="nx">removeClass</span><span class="p">(</span><span class="s1">&#39;open-page&#39;</span><span class="p">).</span><span class="nx">addClass</span><span class="p">(</span><span class="s1">&#39;close-page&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC26" class="line">      <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#titlePage&#39;</span><span class="p">).</span><span class="nx">html</span><span class="p">(</span><span class="s2">&quot;News&quot;</span><span class="p">);</span></span>&#x000A;<span id="LC27" class="line">    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.post&#39;</span><span class="p">).</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;display&#39;</span><span class="p">,</span> <span class="s1">&#39;block&#39;</span><span class="p">);</span></span>&#x000A;<span id="LC28" class="line"></span>&#x000A;<span id="LC29" class="line">  <span class="p">});</span></span>&#x000A;<span id="LC30" class="line"><span class="c1">//logout</span></span>&#x000A;<span id="LC31" class="line"><span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#logout&quot;</span><span class="p">).</span><span class="nx">click</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span> </span>&#x000A;<span id="LC32" class="line">  <span class="nx">$</span><span class="p">.</span><span class="nx">ajax</span><span class="p">({</span></span>&#x000A;<span id="LC33" class="line">            <span class="na">type</span><span class="p">:</span> <span class="s2">&quot;GET&quot;</span><span class="p">,</span></span>&#x000A;<span id="LC34" class="line">            <span class="na">url</span> <span class="p">:</span> <span class="s1">&#39;/user/logout/&#39;</span><span class="p">,</span></span>&#x000A;<span id="LC35" class="line">            <span class="na">dataType</span><span class="p">:</span> <span class="s2">&quot;html&quot;</span><span class="p">,</span>  				</span>&#x000A;<span id="LC36" class="line">            <span class="na">success</span><span class="p">:</span> <span class="kd">function</span> <span class="p">()</span> <span class="p">{</span></span>&#x000A;<span id="LC37" class="line">           	<span class="nb">window</span><span class="p">.</span><span class="nx">location</span><span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="s2">&quot;/user/&quot;</span><span class="p">);</span></span>&#x000A;<span id="LC38" class="line">            <span class="p">},</span></span>&#x000A;<span id="LC39" class="line">          <span class="na">error</span><span class="p">:</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">request</span><span class="p">,</span> <span class="nx">status</span><span class="p">,</span> <span class="nx">error</span><span class="p">)</span> <span class="p">{</span> </span>&#x000A;<span id="LC40" class="line">			  <span class="k">if</span><span class="p">(</span><span class="nx">request</span><span class="p">.</span><span class="nx">status</span><span class="o">===</span><span class="mi">405</span><span class="p">){</span>    </span>&#x000A;<span id="LC41" class="line">					<span class="nx">alert</span><span class="p">(</span><span class="s2">&quot;Please login first&quot;</span><span class="p">);</span> </span>&#x000A;<span id="LC42" class="line">				<span class="p">}</span>            </span>&#x000A;<span id="LC43" class="line">            <span class="p">}</span></span>&#x000A;<span id="LC44" class="line">            </span>&#x000A;<span id="LC45" class="line">    <span class="p">});</span></span>&#x000A;<span id="LC46" class="line">  <span class="p">});</span></span>&#x000A;<span id="LC47" class="line"><span class="c1">//show username</span></span>&#x000A;<span id="LC48" class="line">      	      		   		</span>&#x000A;<span id="LC49" class="line">  <span class="nx">$</span><span class="p">.</span><span class="nx">ajax</span><span class="p">({</span></span>&#x000A;<span id="LC50" class="line">            <span class="na">type</span><span class="p">:</span> <span class="s2">&quot;GET&quot;</span><span class="p">,</span></span>&#x000A;<span id="LC51" class="line">            <span class="na">url</span> <span class="p">:</span> <span class="s1">&#39;/user/get_profile/&#39;</span><span class="p">,</span></span>&#x000A;<span id="LC52" class="line">            <span class="na">dataType</span><span class="p">:</span> <span class="s2">&quot;html&quot;</span><span class="p">,</span> 				</span>&#x000A;<span id="LC53" class="line">            <span class="na">success</span><span class="p">:</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span></span>&#x000A;<span id="LC54" class="line">           <span class="nx">$</span><span class="p">(</span> <span class="s1">&#39;#getusername &#39;</span> <span class="p">).</span><span class="nx">html</span><span class="p">((</span><span class="nx">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">data</span><span class="p">)).</span><span class="nx">username</span><span class="p">);</span> 			</span>&#x000A;<span id="LC55" class="line">            <span class="p">},</span></span>&#x000A;<span id="LC56" class="line">           <span class="na">error</span><span class="p">:</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">request</span><span class="p">)</span> <span class="p">{</span>                </span>&#x000A;<span id="LC57" class="line">				<span class="nx">alert</span><span class="p">(</span><span class="s2">&quot;this user not found&quot;</span><span class="p">);</span>	      	      		</span>&#x000A;<span id="LC58" class="line">      		<span class="p">}</span></span>&#x000A;<span id="LC59" class="line">		<span class="p">});</span></span>&#x000A;<span id="LC60" class="line"><span class="c1">//end show username</span></span>&#x000A;<span id="LC61" class="line"><span class="c1">//change profile</span></span>&#x000A;<span id="LC62" class="line"><span class="kd">function</span> <span class="nx">changeprofile</span><span class="p">(</span><span class="nx">username</span><span class="p">){</span></span>&#x000A;<span id="LC63" class="line">  <span class="nb">document</span><span class="p">.</span><span class="nx">title</span> <span class="o">=</span> <span class="nx">username</span><span class="p">;</span></span>&#x000A;<span id="LC64" class="line">  <span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;usernameitem&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;none&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC65" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;usernameprofitem&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;block&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC66" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;backtoprofile&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;block&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC67" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;logout&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;none&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC68" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;users&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;none&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC69" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;setting&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;none&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC70" class="line">			<span class="nx">$</span><span class="p">(</span> <span class="s1">&#39;#getusernameprof &#39;</span> <span class="p">).</span><span class="nx">html</span><span class="p">(</span><span class="nx">username</span><span class="p">);</span> </span>&#x000A;<span id="LC71" class="line">			 </span>&#x000A;<span id="LC72" class="line"><span class="p">}</span></span>&#x000A;<span id="LC73" class="line"><span class="c1">//go to profile</span></span>&#x000A;<span id="LC74" class="line"><span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#usernamecontact&quot;</span><span class="p">).</span><span class="nx">click</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span> </span>&#x000A;<span id="LC75" class="line"> <span class="kd">var</span> <span class="nx">username</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#usernamecontact&quot;</span><span class="p">).</span><span class="nx">text</span><span class="p">();</span></span>&#x000A;<span id="LC76" class="line">  <span class="nx">$</span><span class="p">.</span><span class="nx">ajax</span><span class="p">({</span></span>&#x000A;<span id="LC77" class="line">            <span class="na">type</span><span class="p">:</span> <span class="s2">&quot;GET&quot;</span><span class="p">,</span></span>&#x000A;<span id="LC78" class="line">            <span class="na">url</span> <span class="p">:</span> <span class="s2">&quot;/user/get_profile/by_username/&quot;</span><span class="o">+</span> <span class="nx">username</span> <span class="o">+</span> <span class="s2">&quot;/&quot;</span><span class="p">,</span></span>&#x000A;<span id="LC79" class="line">            <span class="na">contentType</span><span class="p">:</span> <span class="s2">&quot;application/json&quot;</span><span class="p">,</span></span>&#x000A;<span id="LC80" class="line">            <span class="na">dataType</span><span class="p">:</span> <span class="s2">&quot;html&quot;</span><span class="p">,</span></span>&#x000A;<span id="LC81" class="line">            <span class="na">success</span><span class="p">:</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span></span>&#x000A;<span id="LC82" class="line">			<span class="nx">$</span><span class="p">(</span> <span class="s1">&#39;#getidprof &#39;</span> <span class="p">).</span><span class="nx">html</span><span class="p">((</span><span class="nx">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">data</span><span class="p">)).</span><span class="nx">id</span><span class="p">);</span> 	</span>&#x000A;<span id="LC83" class="line">            <span class="nx">changeprofile</span><span class="p">(</span><span class="nx">username</span><span class="p">);</span></span>&#x000A;<span id="LC84" class="line">             <span class="nb">window</span><span class="p">.</span><span class="nx">history</span><span class="p">.</span><span class="nx">replaceState</span><span class="p">(</span><span class="nx">username</span><span class="p">,</span><span class="nx">username</span><span class="p">,</span> <span class="s2">&quot;/user/&quot;</span><span class="o">+</span> <span class="nx">username</span>  <span class="p">);</span>  </span>&#x000A;<span id="LC85" class="line">            <span class="p">},</span></span>&#x000A;<span id="LC86" class="line">            <span class="na">error</span><span class="p">:</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">request</span><span class="p">,</span> <span class="nx">status</span><span class="p">,</span> <span class="nx">error</span><span class="p">)</span> <span class="p">{</span></span>&#x000A;<span id="LC87" class="line">                    </span>&#x000A;<span id="LC88" class="line">      		 <span class="k">if</span> <span class="p">(</span><span class="nx">request</span><span class="p">.</span><span class="nx">status</span><span class="o">===</span><span class="mi">406</span><span class="p">)</span> </span>&#x000A;<span id="LC89" class="line">             <span class="p">{</span></span>&#x000A;<span id="LC90" class="line">					<span class="nx">alert</span><span class="p">(</span><span class="s2">&quot; the user id does not exist &quot;</span><span class="p">);</span>             </span>&#x000A;<span id="LC91" class="line">             <span class="p">}</span>  </span>&#x000A;<span id="LC92" class="line"></span>&#x000A;<span id="LC93" class="line">            <span class="p">}</span></span>&#x000A;<span id="LC94" class="line">          <span class="p">});</span>          </span>&#x000A;<span id="LC95" class="line">  <span class="p">});</span></span>&#x000A;<span id="LC96" class="line"></span>&#x000A;<span id="LC97" class="line"><span class="c1">// back to profile</span></span>&#x000A;<span id="LC98" class="line"><span class="nx">$</span><span class="p">(</span><span class="s2">&quot;#backtoprofile&quot;</span><span class="p">).</span><span class="nx">click</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span> </span>&#x000A;<span id="LC99" class="line">           	<span class="nb">window</span><span class="p">.</span><span class="nx">location</span><span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="s2">&quot;/user/home/&quot;</span><span class="p">);</span></span>&#x000A;<span id="LC100" class="line">              <span class="nb">document</span><span class="p">.</span><span class="nx">title</span> <span class="o">=</span> <span class="s2">&quot;home&quot;</span><span class="p">;</span></span>&#x000A;<span id="LC101" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;usernameitem&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;block&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC102" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;usernameprofitem&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;none&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC103" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;backtoprofile&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;none&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC104" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;logout&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;block&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC105" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;users&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;block&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC106" class="line">			<span class="nb">document</span><span class="p">.</span><span class="nx">getElementById</span><span class="p">(</span><span class="s1">&#39;setting&#39;</span><span class="p">).</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">=</span> <span class="s1">&#39;block&#39;</span><span class="p">;</span></span>&#x000A;<span id="LC107" class="line">			  <span class="p">});</span></span>&#x000A;<span id="LC108" class="line"> </span>&#x000A;<span id="LC109" class="line">  <span class="p">});</span></span></code></pre>&#x000A;
</div>

</div>

</article>
</div>

</div>

</div>
</div>
</div>
</div>
</div>

<script>
  GitLab.GfmAutoComplete.dataSource = "/ElmosDS/Judge93/autocomplete_sources?type=NilClass&type_id=master%2Fproject%2Fstatics%2Fjs%2FJavaS.js"
  GitLab.GfmAutoComplete.setup();
</script>


</body>
</html>

