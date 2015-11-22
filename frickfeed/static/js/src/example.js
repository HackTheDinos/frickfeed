// TODO: post to specimens endpoint
///////// Record
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
        shipping_point: ''
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
      debugger;
      // TODO: handle validation appropriately
      return;
    }

    // reset input fields on submit
    var resetState = {
        collector_name_first: '',
        collector_name_last: '',
        location: '',
        box: '',
        date_recorded: '',
        date: '',
        season_at: '',
        shipping_point: ''
    }
    this.setState(resetState);
    this.props.onRecordSubmit(this.state);
  },
  render: function() {
    return (
      <form className="recordForm" onSubmit={this.handleSubmit}>
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
        <input type="submit" value="Post" />
      </form>
    );
  }
});

///////// RecordBox
var RecordBox = React.createClass({
  handleRecordSubmit: function(record) {
    // TODO: optimistically append record here

    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: record,
      success: function(data) {
        // TODO: handle successful record post req appropriately
        debugger;
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    return (
      <div className="recordBox">
        <RecordForm onRecordSubmit={this.handleRecordSubmit} />
      </div>
    );
  }
});

///////// render RecordBox
ReactDOM.render(
  <RecordBox url="/v1/records/" />,
  document.getElementById('content')
);