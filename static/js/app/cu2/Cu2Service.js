eventosModule.service('cu2Service', ['$q', '$http', function($q, $http) {

    this.AVerEventosInscritos = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/AVerEventosInscritos',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventosInscritos", "/VPrincipalUsuario", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VPrincipalUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/VPrincipalUsuario',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AVerEventosNoInscritos = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/AVerEventosNoInscritos',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventosNoInscritos", "/VPrincipalUsuario", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VEventosInscritos = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/VEventosInscritos',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AVerEventoInscrito = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/AVerEventoInscrito',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventoInscrito", "/VEventosInscritos", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VEventoInscrito = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/VEventoInscrito',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACertificado = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/ACertificado',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventoInscrito", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VEventosNoInscritos = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/VEventosNoInscritos',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACredencial = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/ACredencial',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventoInscrito", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AVerEventoNoInscrito = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/AVerEventoNoInscrito',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventoNoInscrito", "/VEventosNoInscritos", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VEventoNoInscrito = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/VEventoNoInscrito',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AReservarEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu2/AReservarEvento',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventosInscritos", "/VEventosNoInscritos", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);