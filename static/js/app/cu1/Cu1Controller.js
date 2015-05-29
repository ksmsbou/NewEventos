eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VPrincipalAdministrador', {
                controller: 'VPrincipalAdministradorController',
                templateUrl: 'app/cu1/VPrincipalAdministrador.html'
            }).when('/VVerEvento', {
                controller: 'VVerEventoController',
                templateUrl: 'app/cu1/VVerEvento.html'
            }).when('/VModificarEvento/:id', {
                controller: 'VModificarEventoController',
                templateUrl: 'app/cu1/VModificarEvento.html'
            }).when('/VCrearEvento', {
                controller: 'VCrearEventoController',
                templateUrl: 'app/cu1/VCrearEvento.html'
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
          var tableFields = [["idEvento","Evento"], ["nombre","Nombre"], ["fecha","Fecha"]];
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
              var APersonaAsistio2Data = $scope.res.data2;
              if(typeof APersonaAsistio2Data === 'undefined') APersonaAsistio2Data=[];
              $scope.tableParams2 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: APersonaAsistio2Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(APersonaAsistio2Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VModificarEvento0 = function(id) {
        $location.path('/VModificarEvento/'+id);
      };
      $scope.AEliminarEvento1 = function() {
          
        cu1Service.AEliminarEvento().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ASalir3 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.APersonaAsistio2 = function(id) {
          var tableFields = [["idPersona","idPersona"]];
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
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'ngDialog', 'cu1Service', 'cu3Service',
    function ($scope, $location, $route, flash, $routeParams, ngDialog, cu1Service, cu3Service) {
      $scope.msg = '';
      $scope.fEvento = {};

      cu1Service.VModificarEvento({"id":$routeParams.id}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.ASalir1 = function() {
          
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
      $scope.ASalir1 = function() {
          
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
