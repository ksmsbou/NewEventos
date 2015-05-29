eventosModule.service('cu1Service', ['$q', '$http', function($q, $http) {

    this.AVerEventosAdmin = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/AVerEventosAdmin',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VPrincipalAdministrador", "/VPrincipalAdministrador", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VPrincipalAdministrador = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/VPrincipalAdministrador',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearEvento = function(fEvento) {
        return  $http({
          url: "cu1/ACrearEvento",
          data: fEvento,
          method: 'POST',
          headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: function (data, headersGetter) {
                var formData = new FormData();
                angular.forEach(data, function (value, key) {
                    formData.append(key, value);
                });

                var headers = headersGetter();
                delete headers['Content-Type'];

                return formData;
          }    });
    //    var labels = ["/VPrincipalAdministrador", "/VCrearEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/VCrearEvento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AVerEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/AVerEvento',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VVerEvento", "/VPrincipalAdministrador", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VVerEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/VVerEvento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AEliminarEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/AEliminarEvento',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VPrincipalAdministrador", "/VVerEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.APersonaAsistio = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/APersonaAsistio',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VVerEvento", "/VVerEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VModificarEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cu1/VModificarEvento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AModificarEvento = function(fEvento) {
        return  $http({
          url: "cu1/AModificarEvento",
          data: fEvento,
          method: 'POST',
          headers: { 'Content-Type': 'multipart/form-data' },
          transformRequest: function (data, headersGetter) {
                var formData = new FormData();
                angular.forEach(data, function (value, key) {
                    formData.append(key, value);
                });

                var headers = headersGetter();
                delete headers['Content-Type'];

                return formData;
          }    });
    //    var labels = ["/VVerEvento", "/VModificarEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);