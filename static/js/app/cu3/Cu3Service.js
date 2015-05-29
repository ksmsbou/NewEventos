eventosModule.service('cu3Service', ['$q', '$http', function($q, $http) {

    this.ARegistro = function(fRegistro) {
        return  $http({
          url: "cu3/ARegistro",
          data: fRegistro,
          method: 'POST',
        });
    //    var labels = ["/VPrincipal", "/VRegistro", "/VPrincipal", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VPrincipal = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu3/VPrincipal',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AIdentificacion = function(fUsuario) {
        return  $http({
          url: "cu3/AIdentificacion",
          data: fUsuario,
          method: 'POST',
        });
    //    var labels = ["/VPrincipalUsuario", "/VPrincipal", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VRegistro = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu3/VRegistro',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ASalir = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu3/ASalir',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VPrincipal", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);