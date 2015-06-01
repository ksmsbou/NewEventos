eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VPrincipalAdministrador', {
                controller: 'VPrincipalAdministradorController',
                templateUrl: 'app/cu1/VPrincipalAdministrador.html'
            }).when('/VCrearEvento', {
                controller: 'VCrearEventoController',
                templateUrl: 'app/cu1/VCrearEvento.html'
            }).when('/VVerEvento', {
                controller: 'VVerEventoController',
                templateUrl: 'app/cu1/VVerEvento.html'
            }).when('/VModificarEvento', {
                controller: 'VModificarEventoController',
                templateUrl: 'app/cu1/VModificarEvento.html'
            });
});

eventosModule.controller('VPrincipalAdministradorController', 
   ['$scope', '$location', '$route', 'flash', 'ngTableParams', 'cu1Service', 'cu3Service',
    function ($scope, $location, $route, flash, ngTableParams, cu1Service, cu3Service) {
      $scope.msg = '';
      cu1Service.VPrincipalAdministrador().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var AVerEvento1Data = $scope.res.data1;
              if(typeof AVerEvento1Data === 'undefined') AVerEvento1Data=[];
              $scope.tableParams1 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: AVerEvento1Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(AVerEvento1Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VCrearEvento0 = function() {
        $location.path('/VCrearEvento');
      };
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.AVerEvento1 = function(id) {
          var tableFields = [["idEvento","id"], ["nombre","Nombre"], ["fecha","Fecha"]];
          var arg = {};
          arg[tableFields[0][1]] = ((typeof id === 'object')?JSON.stringify(id):id);
          cu1Service.AVerEvento(arg).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
      };

    }]);
eventosModule.controller('VCrearEventoController', 
   ['$scope', '$location', '$route', 'flash', 'ngDialog', 'cu1Service', 'cu3Service',
    function ($scope, $location, $route, flash, ngDialog, cu1Service, cu3Service) {
      $scope.msg = '';
      $scope.fEvento = {};

      cu1Service.VCrearEvento().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VPrincipalAdministrador1 = function() {
        $location.path('/VPrincipalAdministrador');
      };
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.fEventoSubmitted = false;
      $scope.ACrearEvento0 = function(isValid) {
        $scope.fEventoSubmitted = true;
        if (isValid) {
          
          cu1Service.ACrearEvento($scope.fEvento).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.__ayuda = function() {
ngDialog.open({ template: 'ayuda_VCrearEvento.html',
        showClose: true, closeByDocument: true, closeByEscape: true});
}    }]);
eventosModule.controller('VVerEventoController', 
   ['$scope', '$location', '$route', 'flash', 'ngTableParams', 'cu1Service', 'cu3Service',
    function ($scope, $location, $route, flash, ngTableParams, cu1Service, cu3Service) {
      $scope.msg = '';
      cu1Service.VVerEvento().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var APersonaAsistio3Data = $scope.res.data3;
              if(typeof APersonaAsistio3Data === 'undefined') APersonaAsistio3Data=[];
              $scope.tableParams3 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: APersonaAsistio3Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(APersonaAsistio3Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VModificarEvento0 = function() {
        $location.path('/VModificarEvento');
      };
      $scope.AEliminarEvento1 = function() {
          
        cu1Service.AEliminarEvento().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VPrincipalAdministrador4 = function() {
        $location.path('/VPrincipalAdministrador');
      };
      $scope.ASalir5 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.APersonaAsistio3 = function(id) {
          var tableFields = [["idPersona","id"], ["nombres","Nombre"], ["apellidos","Apellidos"]];
          var arg = {};
          arg[tableFields[0][1]] = ((typeof id === 'object')?JSON.stringify(id):id);
          cu1Service.APersonaAsistio(arg).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
      };

    }]);
eventosModule.controller('VModificarEventoController', 
   ['$scope', '$location', '$route', 'flash', 'ngDialog', 'cu1Service', 'cu3Service',
    function ($scope, $location, $route, flash, ngDialog, cu1Service, cu3Service) {
      $scope.msg = '';
      $scope.fEvento = {};

      cu1Service.VModificarEvento().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VVerEvento1 = function() {
        $location.path('/VVerEvento');
      };
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.fEventoSubmitted = false;
      $scope.AModificarEvento0 = function(isValid) {
        $scope.fEventoSubmitted = true;
        if (isValid) {
          
          cu1Service.AModificarEvento($scope.fEvento).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.__ayuda = function() {
ngDialog.open({ template: 'ayuda_VModificarEvento.html',
        showClose: true, closeByDocument: true, closeByEscape: true});
}    }]);
