eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VPrincipal', {
                controller: 'VPrincipalController',
                templateUrl: 'app/cu3/VPrincipal.html'
            }).when('/VRegistro', {
                controller: 'VRegistroController',
                templateUrl: 'app/cu3/VRegistro.html'
            });
});

eventosModule.controller('VPrincipalController', 
   ['$scope', '$location', '$route', 'flash', 'cu1Service', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu1Service, cu2Service, cu3Service) {
      $scope.msg = '';
      $scope.fUsuario = {};

      cu3Service.VPrincipal().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VRegistro0 = function() {
        $location.path('/VRegistro');
      };

      $scope.fUsuarioSubmitted = false;
      $scope.AIdentificacion1 = function(isValid) {
        $scope.fUsuarioSubmitted = true;
        if (isValid) {
          
          cu3Service.AIdentificacion($scope.fUsuario).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
eventosModule.controller('VRegistroController', 
   ['$scope', '$location', '$route', 'flash', 'cu1Service', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu1Service, cu2Service, cu3Service) {
      $scope.msg = '';
      $scope.fRegistro = {};

      cu3Service.VRegistro().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VPrincipal0 = function() {
        $location.path('/VPrincipal');
      };

      $scope.fRegistroSubmitted = false;
      $scope.ARegistro1 = function(isValid) {
        $scope.fRegistroSubmitted = true;
        if (isValid) {
          
          cu3Service.ARegistro($scope.fRegistro).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
