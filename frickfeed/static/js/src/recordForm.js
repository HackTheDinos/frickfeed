///////// Record /////////
var RecordForm = React.createClass({
  getInitialState: function() {
    // TODO: make resetState a constant
    var resetState = {
        collector_name_first: '',
        collector_name_last: '',
        location: '',
        box: '',
        date_recorded: '',
        date: '',
        season_at: '',
        shipping_point: '',
        specimens: []
    }
    return resetState;
  },
  handleFirstNameChange: function(e) {
    this.setState({collector_name_first: e.target.value});
  },
  handleLastNameChange: function(e) {
    this.setState({collector_name_last: e.target.value});
  },
  handleLocationChange: function(e) {
    this.setState({location: e.target.value});
  },
  handleBoxChange: function(e) {
    this.setState({box: e.target.value});
  },
  handleShippingPointChange: function(e) {
    this.setState({shipping_point: e.target.value});
  },
  handleDateRecordedChange: function(e) {
    this.setState({date_recorded: e.target.value});
  },
  handleDateChange: function(e) {
    this.setState({date: e.target.value});
  },
  handleSeasonAtChange: function(e) {
    this.setState({season_at: e.target.value});
  },
  handleSpecimenChange: function(specimenState) {
    // specimens are uniquely identified by client_identifier
    for(var i=0; i < this.state.specimens.length; i++) {
        if ( this.state.specimens[i].client_identifier === specimenState.client_identifier ) {
            this.state.specimens[i] = specimenState;
            return;
        }
    }
    this.state.specimens.push(specimenState);
  },
  handleSubmit: function(e) {
    e.preventDefault();
    // validate fields are filled
    var collector_name_first = this.state.collector_name_first.trim();
    var collector_name_last = this.state.collector_name_last.trim();
    var location = this.state.location.trim();
    var box = this.state.box.trim();
    var date_recorded = this.state.date_recorded.trim();
    var date = this.state.date.trim();
    var season_at = this.state.season_at.trim();
    var shipping_point = this.state.shipping_point.trim();

    // TODO: validate by iterating through these and calling a validate function
    if (!collector_name_first || !collector_name_last || !location || !box || !date_recorded || !date || !season_at || !shipping_point ) {
      // TODO: handle validation appropriately
      return;
    }

    // TODO: fire dispatcher event to delete specimens

    // reset input fields on submit
    var resetState = {
        collector_name_first: '',
        collector_name_last: '',
        location: '',
        box: '',
        date_recorded: '',
        date: '',
        season_at: '',
        shipping_point: '',
        specimens: []
    }
    this.setState(resetState);
    this.props.onRecordSubmit(this.state);
  },
  render: function() {
    var specimenProps = {
        onChange: this.handleSpecimenChange
    }
    return (
      <form className="recordForm" onSubmit={this.handleSubmit}>
        <h2>Record Details</h2>
        <input
          type="text"
          placeholder="First name"
          value={this.state.collector_name_first}
          onChange={this.handleFirstNameChange}
        />
        <input
          type="text"
          placeholder="Last name"
          value={this.state.collector_name_last}
          onChange={this.handleLastNameChange}
        />
        <input
          type="text"
          placeholder="Location"
          value={this.state.location}
          onChange={this.handleLocationChange}
        />
        <input
          type="number"
          placeholder="Box no."
          value={this.state.box}
          onChange={this.handleBoxChange}
        />
        <input
          type="text"
          placeholder="Shipping point"
          value={this.state.shipping_point}
          onChange={this.handleShippingPointChange}
        />
        <input
          type="date"
          placeholder="Date recorded"
          value={this.state.date_recorded}
          onChange={this.handleDateRecordedChange}
        />
        <input
          type="date"
          placeholder="Date"
          value={this.state.date}
          onChange={this.handleDateChange}
        />
        <input
          type="string"
          placeholder="Season at"
          value={this.state.season_at}
          onChange={this.handleSeasonAtChange}
        />
        <SpecimenInputFields {...specimenProps} />
        <input type="submit" value="Save" />
      </form>
    );
  }
});
