///////// RecordBox /////////
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

///////// render RecordBox /////////
ReactDOM.render(
  <RecordBox url="/v1/records/" />,
  document.getElementById('content')
);