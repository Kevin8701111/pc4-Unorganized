const Router = require('koa-router');
const userctrl = require('../controllers/users/UserController');
const router = new Router({prefix: '/api/user'});

const dbControl = require('../lib/mysql_control')

router.get('/',)

// router.post('/apiUserLogin', userctrl.login) //rest api
router.post('/login', userctrl.login) //restful api
router.get('/userinfo', userctrl.userInfo);


module.exports = router;
