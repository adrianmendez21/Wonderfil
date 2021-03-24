var express = require('express');
var router = express.Router();
//var calculations = require('../calculations.js');

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

router.get('/dispense', function(req, res) {
  res.json({name: "Wonderfil", working:true});
});

module.exports = router;
