/**
 * DeRegNet REST API
 * DeRegNet REST API 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: deregnet@informatik.uni-tuebingen.de
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.DeRegNetRestApi);
  }
}(this, function(expect, DeRegNetRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DeRegNetRestApi.Score();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Score', function() {
    it('should create an instance of Score', function() {
      // uncomment below and update the code to test Score
      //var instane = new DeRegNetRestApi.Score();
      //expect(instance).to.be.a(DeRegNetRestApi.Score);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instane = new DeRegNetRestApi.Score();
      //expect(instance).to.be();
    });

    it('should have the property nodeIds (base name: "node_ids")', function() {
      // uncomment below and update the code to test the property nodeIds
      //var instane = new DeRegNetRestApi.Score();
      //expect(instance).to.be();
    });

    it('should have the property scoreValues (base name: "score_values")', function() {
      // uncomment below and update the code to test the property scoreValues
      //var instane = new DeRegNetRestApi.Score();
      //expect(instance).to.be();
    });

  });

}));