///////// CommentList
var CommentList = React.createClass({
  render: function() {
    debugger;
    var commentNodes = this.props.data.map(function(record) {
      return (
        <Comment season_at={record.season_at} key={record.id}>
          {record.collector_name}
        </Comment>
      );
    });
    return (
      <div className="commentList">
        {commentNodes}
      </div>
    );
  }
});

///////// CommentForm
var CommentForm = React.createClass({
  getInitialState: function() {
    return {season_at: ''};
  },
  handleAuthorChange: function(e) {
    this.setState({author: e.target.value});
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var author = this.state.author.trim();
    // TODO: add more vars
    // var text = this.state.text.trim();
    // var text = this.state.text.trim();

    if (!author) {
      return;
    }
    // TODO: send request to the server
    this.setState({author: ''});
    this.props.onCommentSubmit({author: author});
  },
  render: function() {
    return (
      <form className="commentForm" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Your name"
          value={this.state.author}
          onChange={this.handleAuthorChange}
        />
        <input type="submit" value="Post" />
      </form>
    );
  }
});

///////// CommentBox
var CommentBox = React.createClass({
  loadCommentsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  handleCommentSubmit: function(record) {
    record.location = "test";
    record.box = Math.floor(Math.random() * 100);
    record.shipping_point = "NY";
    record.date_recorded = "2015-01-01";
    record.date = "1970-01-01";
    record.season_at = "salt n peppaaaa";
    record.collector_name_first = "bob";
    record.collector_name_last = "loblaw";

    // var comments = this.state.data;
    // // Optimistically set an id on the new comment. It will be replaced by an
    // // id generated by the server. In a production application you would likely
    // // not use Date.now() for this and would have a more robust system in place.
    // data.id = Date.now();
    // debugger;
    // var newComments = comments.concat([data]);
    // this.setState({data: newComments});

    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: record,
      success: function(data) {
        this.state.data.push(data)
        this.setState({author: ''}); // clear input field
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadCommentsFromServer();
    setInterval(this.loadCommentsFromServer, this.props.pollInterval);
  },
  render: function() {
    debugger;
    return (
      <div className="commentBox">
        <h1>Comments</h1>
        <CommentList data={this.state.data} />
        <CommentForm onCommentSubmit={this.handleCommentSubmit} />
      </div>
    );
  }
});

///////// Comment
var Comment = React.createClass({
  // rawMarkup: function() {
  //   var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
  //   return { __html: rawMarkup };
  // },

  render: function() {
    return (
      <div className="comment">
        <h2 className="commentAuthor">
          {this.props.season_at}
        </h2>
      </div>
    );
  }
});

// Dummy data
var data = [
  {id: 1, author: "Pete Hunt", text: "This is one comment"},
  {id: 2, author: "Jordan Walke", text: "This is *another* comment"}
];

///////// render CommentBox
ReactDOM.render(
  <CommentBox url="/v1/records/" pollInterval={2000} />,
  document.getElementById('content')
);