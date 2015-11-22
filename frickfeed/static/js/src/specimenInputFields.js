///////// SpecimenInputFields /////////
// TODO: add flux for adding and deleting comments
var SpecimenInputFields = React.createClass({
  getInitialState: function() {
    var resetState = {
        client_identifier: (Math.random() * 1000000).toString(),
        amnh_catalog_a: '',
        amnh_catalog_b: '',
        field_no: '',
        description: '',
        location: '',
    };
    return resetState;
  },
  handleAmnhCatalogAChange: function(e) {
    debugger;
    this.setState({amnh_catalog_a: e.target.value});
    this.props.onChange(this.state);
  },
  handleAmnhCatalogBChange: function(e) {
    this.setState({amnh_catalog_b: e.target.value});
    this.props.onChange(this.state);
  },
  handleFieldNoChange: function(e) {
    this.setState({field_no: e.target.value});
    this.props.onChange(this.state);
  },
  handleDescriptionChange: function(e) {
    this.setState({description: e.target.value});
    this.props.onChange(this.state);
  },
  handleLocationChange: function(e) {
    this.setState({location: e.target.value});
    this.props.onChange(this.state);
  },
  render: function() {
    return (
    <section class="kitten" id="kitten">
        <h3>Specimen Details</h3>
        <input
          type="text"
          placeholder="AMNH Catalog A"
          value={this.state.amnh_catalog_a}
          onChange={this.handleAmnhCatalogAChange}
        />
        <input
          type="text"
          placeholder="AMNH Catalog B"
          value={this.state.amnh_catalog_b}
          onChange={this.handleAmnhCatalogBChange}
        />
        <input
          type="number"
          placeholder="Field No."
          value={this.state.field_no}
          onChange={this.handleFieldNoChange}
        />
        <input
          type="text"
          placeholder="Description"
          value={this.state.description}
          onChange={this.handleDescriptionChange}
        />
        <input
          type="text"
          placeholder="Location"
          value={this.state.location}
          onChange={this.handleLocationChange}
        />
    </section>
    );
  }
});